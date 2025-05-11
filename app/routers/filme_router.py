from fastapi import APIRouter, HTTPException
from typing import List
from app.models.filme_model import Filme  # Importando o modelo de dados
from typing import Optional

router = APIRouter(prefix="/filmes", tags=["Filmes"])

# Banco de dados fake para armazenar os filmes
filmes_fake_db = {}

@router.get("/", response_model=List[Filme])
async def listar_filmes():
    """Listar todos os filmes"""
    return list(filmes_fake_db.values())

@router.get("/{filme_id}", response_model=Filme)
async def buscar_filme(filme_id: str):
    """Buscar filme por ID"""
    filme = filmes_fake_db.get(filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

@router.post("/", response_model=Filme)
async def criar_filme(filme: Filme):
    """Criar um novo filme"""
    if filme.titulo in [f.titulo for f in filmes_fake_db.values()]:
        raise HTTPException(status_code=400, detail="Filme já existe")
    filmes_fake_db[filme.titulo] = filme
    return filme

@router.put("/{filme_id}", response_model=Filme)
async def atualizar_filme(filme_id: str, filme: Filme):
    """Atualizar filme existente"""
    if filme_id not in filmes_fake_db:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    filmes_fake_db[filme_id] = filme
    return filme

@router.delete("/{filme_id}")
async def deletar_filme(filme_id: str):
    """Deletar um filme"""
    if filme_id not in filmes_fake_db:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    del filmes_fake_db[filme_id]
    return {"detail": "Filme deletado com sucesso"}
