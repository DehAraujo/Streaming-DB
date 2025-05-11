from fastapi import APIRouter, HTTPException
from typing import List
from app.models.playlist_model import Playlist  # Importando o modelo de dados
from datetime import datetime

router = APIRouter(prefix="/playlists", tags=["Playlists"])

# Banco de dados fake para armazenar as playlists
playlists_fake_db = {}

@router.get("/", response_model=List[Playlist])
async def listar_playlists():
    """Listar todas as playlists"""
    return list(playlists_fake_db.values())

@router.get("/{playlist_id}", response_model=Playlist)
async def buscar_playlist(playlist_id: int):
    """Buscar playlist por ID"""
    playlist = playlists_fake_db.get(playlist_id)
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist não encontrada")
    return playlist

@router.post("/", response_model=Playlist)
async def criar_playlist(playlist: Playlist):
    """Criar uma nova playlist"""
    if playlist.usuario_id in [p.usuario_id for p in playlists_fake_db.values()] and playlist.nome in [p.nome for p in playlists_fake_db.values()]:
        raise HTTPException(status_code=400, detail="Playlist com esse nome já existe para esse usuário")
    playlist.criada_em = datetime.utcnow()
    playlists_fake_db[playlist.nome] = playlist  # Chave pode ser o nome da playlist ou um ID único
    return playlist

@router.put("/{playlist_id}", response_model=Playlist)
async def atualizar_playlist(playlist_id: int, playlist: Playlist):
    """Atualizar playlist existente"""
    if playlist_id not in playlists_fake_db:
        raise HTTPException(status_code=404, detail="Playlist não encontrada")
    playlists_fake_db[playlist_id] = playlist
    return playlist

@router.delete("/{playlist_id}")
async def deletar_playlist(playlist_id: int):
    """Deletar uma playlist"""
    if playlist_id not in playlists_fake_db:
        raise HTTPException(status_code=404, detail="Playlist não encontrada")
    del playlists_fake_db[playlist_id]
    return {"detail": "Playlist deletada com sucesso"}
