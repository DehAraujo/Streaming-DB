from pydantic import BaseModel
from datetime import datetime

class Playlist(BaseModel):
    tipo: str = "playlist"
    usuario_id: int
    nome: str
    privada: bool
    criada_em: datetime
