from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Avaliacao(BaseModel):
    tipo: str = "avaliacao"
    usuario_id: int
    conteudo_id_mongo: str
    nota: int  # de 1 a 5
    comentario: Optional[str] = None
    data_avaliacao: datetime
