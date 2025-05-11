from pydantic import BaseModel
from datetime import datetime

class Visualizacao(BaseModel):
    tipo: str = "visualizacao"
    usuario_id: int
    conteudo_id_mongo: str
    data_visualizacao: datetime
    progresso: int  # em percentual ou segundos
