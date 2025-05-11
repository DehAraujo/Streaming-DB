from pydantic import BaseModel
from typing import Optional, List


class Filme(BaseModel):
    tipo: str = "filme"
    titulo: str
    genero: str
    ano_lancamento: int
    duracao: int
    sinopse: str
    diretor: List[str]
    elenco: Optional[list[str]] = None
