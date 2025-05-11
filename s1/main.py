from faker import Faker
from kafka import KafkaProducer
import json
import random
import time
from app.models import PlaylistConteudo  # ou o caminho correto onde a classe está definida
from app.models import Playlist
from app.models import Avaliacao
from app.models import Visualizacao
from app.models import Usuario

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v.dict()).encode('utf-8')
)

# Função para gerar dados aleatórios
def gerar_dado():
    tipo = random.choice(["filme", "serie", "usuario", "avaliacao", "visualizacao", "playlist", "playlist_conteudo"])

    if tipo == "filme":
        return {
            "tipo": "catalogo",
            "subtipo": "filme",
            "titulo": fake.sentence(nb_words=3),
            "descricao": fake.text(),
            "ano": random.randint(1980, 2024),
            "genero": random.choice(["Ação", "Drama", "Comédia", "Terror"])
        }
    elif tipo == "serie":
        temporadas = random.randint(1, 10)
        return {
            "tipo": "catalogo",
            "subtipo": "serie",
            "titulo": fake.sentence(nb_words=3),
            "descricao": fake.text(),
            "temporadas": temporadas,
            "episodios_por_temporada": [random.randint(6, 15) for _ in range(temporadas)],
            "genero": random.choice(["Ação", "Drama", "Comédia", "Suspense"])
        }
    elif tipo == "usuario":
        return Usuario(
            nome=fake.name(),
            senha=fake.password(),
            email=fake.email(),
            data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=90),
            ativo=random.choice([True, False])
        )
    elif tipo == "avaliacao":
        return Avaliacao(
            usuario_id=random.randint(1, 1000),
            conteudo_id_mongo=fake.uuid4(),
            nota=random.randint(1, 5),
            comentario=fake.text() if random.random() > 0.5 else None,
            data_avaliacao=fake.date_this_decade()
        )
    elif tipo == "visualizacao":
        return Visualizacao(
            usuario_id=random.randint(1, 1000),
            conteudo_id_mongo=fake.uuid4(),
            data_visualizacao=fake.date_this_decade(),
            progresso=random.randint(1, 100)
        )
    elif tipo == "playlist":
        return Playlist(
            usuario_id=random.randint(1, 1000),
            nome=fake.sentence(nb_words=3),
            privada=random.choice([True, False]),
            criada_em=fake.date_this_decade()
        )
    elif tipo == "playlist_conteudo":
        return PlaylistConteudo(
            playlist_id=random.randint(1, 1000),
            conteudo_id_mongo=fake.uuid4(),
            adicionado_em=fake.date_this_decade()
        )

# Enviar dados para o Kafka
while True:
    dado = gerar_dado()
    producer.send("streaming_topico", dado)
    time.sleep(1)

