from fastapi import FastAPI
from app.routers import (
    usuario_router,
    filme_router,
    serie_router,
    playlist_router,
    playlistConteudo_router,
    visualizacao_router,
    avaliacao_router,
    favoritos_router,
)
from data import data  # Supondo que seja algum mock de dados ou inicialização

app = FastAPI(
    title="Plataforma de Streaming",
    description="API para gerenciamento de usuários, filmes, séries, playlists e mais",
    version="1.0.0",
)

# Registro de todas as rotas
app.include_router(usuario_router.router)
app.include_router(filme_router.router)
app.include_router(serie_router.router)
app.include_router(playlist_router.router)
app.include_router(playlistConteudo_router.router)
app.include_router(visualizacao_router.router)
app.include_router(avaliacao_router.router)
app.include_router(favoritos_router.router)
