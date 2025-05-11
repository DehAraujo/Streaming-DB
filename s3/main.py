from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração do Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")

# Função para indexar o evento no Elasticsearch
def indexar_no_elasticsearch(dado):
    try:
        es.index(index="catalogo", document=dado)
        logger.info(f"Documento indexado com sucesso: {dado['conteudo_id']}")
    except Exception as e:
        logger.error(f"Erro ao indexar no Elasticsearch: {e}")

# Função principal para consumir eventos do Kafka
def consumir_eventos_kafka():
    consumer = KafkaConsumer(
        'streaming_topico',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    
    for msg in consumer:
        dado = msg.value
        logger.info(f"Evento recebido: {dado}")
        
        if dado.get("tipo") == "catalogo":
            indexar_no_elasticsearch(dado)
        else:
            logger.warning(f"Tipo de evento desconhecido: {dado.get('tipo')}")

if __name__ == "__main__":
    consumir_eventos_kafka()
