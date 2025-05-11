from app.routers import usuario_router  # Importe as rotas do usuário
from data import data  # Caminho absoluto para o módulo
from fastapi import FastAPI


app = FastAPI()

# Registre as rotas
app.include_router(usuario_router.router)