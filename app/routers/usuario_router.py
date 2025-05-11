from fastapi import APIRouter, HTTPException
from typing import List
from app.models.usuario_model import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

# Banco de dados fake para armazenar os usuários
usuarios_fake_db = {}

@router.get("/", response_model=List[Usuario])
async def listar_usuarios():
    """Listar todos os usuários"""
    return list(usuarios_fake_db.values())

@router.get("/{usuario_id}", response_model=Usuario)
async def buscar_usuario(usuario_id: str):
    """Buscar usuário por ID"""
    usuario = usuarios_fake_db.get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.post("/", response_model=Usuario)
async def criar_usuario(usuario: Usuario):
    """Criar um novo usuário"""
    if usuario.email in [u.email for u in usuarios_fake_db.values()]:
        raise HTTPException(status_code=400, detail="Já existe um usuário com esse e-mail")
    usuarios_fake_db[usuario.email] = usuario
    return usuario

@router.put("/{usuario_id}", response_model=Usuario)
async def atualizar_usuario(usuario_id: str, usuario: Usuario):
    """Atualizar usuário existente"""
    if usuario_id not in usuarios_fake_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuarios_fake_db[usuario_id] = usuario
    return usuario

@router.delete("/{usuario_id}")
async def deletar_usuario(usuario_id: str):
    """Deletar um usuário"""
    if usuario_id not in usuarios_fake_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    del usuarios_fake_db[usuario_id]
    return {"detail": "Usuário deletado com sucesso"}
