from kafka import KafkaConsumer
import json
import logging
from db import (
    mongodb,
    postgresql,
    redis as redis_db,
    elasticsearch as es_db
)

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka Consumer
consumer = KafkaConsumer(
    'streaming_topico',
    bootstrap_servers='localhost:9092',
    group_id='streaming-consumer',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Função de processamento
def processar_mensagem(dado):
    t = dado["tipo"]
    try:
        if t == "catalogo" and dado["subtipo"] in ["filme", "serie"]:
            mongodb.inserir_conteudo(dado)
            logger.info(f"Conteúdo {dado['titulo']} inserido no MongoDB.")

        elif t == "usuario":
            postgresql.insert_usuario(
                dado["nome"], dado["senha"], dado["email"],
                dado["data_nascimento"], dado["ativo"]
            )
            logger.info(f"Usuário {dado['nome']} inserido no PostgreSQL.")

        elif t == "avaliacao":
            postgresql.insert_avaliacao(
                dado["usuario_id"], dado["conteudo_id_mongo"],
                dado["nota"], dado.get("comentario", ""), dado["data_avaliacao"]
            )
            logger.info(f"Avaliação para conteúdo {dado['conteudo_id_mongo']} inserida.")

        elif t == "visualizacao":
            redis_db.registrar_visualizacao(
                dado["usuario_id"], dado["conteudo_id_mongo"], dado["progresso"]
            )
            logger.info(f"Visualização registrada para {dado['conteudo_id_mongo']}.")

            # (Opcional) indexar no Elasticsearch
            es_db.indexar_evento({
                "conteudo_id": dado["conteudo_id_mongo"],
                "usuario_id": dado["usuario_id"],
                "tipo_evento": "visualizacao",
                "progresso": dado["progresso"],
                "data_evento": dado["timestamp"]
            })

        elif t == "playlist":
            postgresql.insert_playlist(
                dado["usuario_id"], dado["nome"], dado["privada"], dado["criada_em"]
            )
            logger.info(f"Playlist '{dado['nome']}' criada.")

        elif t == "playlist_conteudo":
            redis_db.adicionar_conteudo_playlist(
                dado["playlist_id"], dado["conteudo_id_mongo"], dado["adicionado_em"]
            )
            logger.info(f"Conteúdo {dado['conteudo_id_mongo']} adicionado à playlist {dado['playlist_id']}.")

        else:
            logger.warning(f"Tipo desconhecido: {t}")

    except Exception as e:
        logger.error(f"Erro ao processar {t}: {e}")

# Loop de consumo
for mensagem in consumer:
    processar_mensagem(mensagem.value)
