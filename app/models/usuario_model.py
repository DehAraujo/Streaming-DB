from pydantic import BaseModel, EmailStr
from datetime import date

class Usuario(BaseModel):
    tipo: str = "usuario"
    nome: str
    senha: str
    email: EmailStr
    data_nascimento: date
    ativo: bool
