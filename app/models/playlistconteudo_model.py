from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PlaylistConteudo(BaseModel):
    playlist_id: int
    conteudo_id: int
    usuario_id: int
    adicionada_em: datetime = datetime.utcnow()

