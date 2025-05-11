from pydantic import BaseModel
from typing import Union

# Modelos importados
from .filme_model import Filme
from .serie_model import Serie
from .usuario_model import Usuario

class Favoritos(BaseModel):
    usuario_id: int
    favorito: Union[Filme, Serie]  # Pode ser um Filme ou uma Série

    class Config:
        orm_mode = True
