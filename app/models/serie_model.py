from pydantic import BaseModel
from typing import List

class Serie(BaseModel):
    tipo: str = "serie"
    titulo: str
    descricao: str
    temporadas: int
    episodios_por_temporada: List[int]
    genero: str
