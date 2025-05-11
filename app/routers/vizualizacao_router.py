from fastapi import APIRouter, HTTPException
from typing import List
from app.models.visualizacao_model import Visualizacao

router = APIRouter(prefix="/visualizacoes", tags=["Visualizações"])

# Banco de dados fake para armazenar as visualizações
visualizacoes_fake_db = {}

@router.get("/", response_model=List[Visualizacao])
async def listar_visualizacoes():
    """Listar todas as visualizações"""
    return list(visualizacoes_fake_db.values())

@router.get("/{conteudo_id_mongo}", response_model=Visualizacao)
async def buscar_visualizacao(conteudo_id_mongo: str):
    """Buscar visualização por conteudo_id_mongo"""
    visualizacao = visualizacoes_fake_db.get(conteudo_id_mongo)
    if not visualizacao:
        raise HTTPException(status_code=404, detail="Visualização não encontrada")
    return visualizacao

@router.post("/", response_model=Visualizacao)
async def criar_visualizacao(visualizacao: Visualizacao):
    """Criar uma nova visualização"""
    if visualizacao.conteudo_id_mongo in visualizacoes_fake_db:
        raise HTTPException(status_code=400, detail="Visualização já existe para esse conteúdo")
    visualizacoes_fake_db[visualizacao.conteudo_id_mongo] = visualizacao
    return visualizacao

@router.put("/{conteudo_id_mongo}", response_model=Visualizacao)
async def atualizar_visualizacao(conteudo_id_mongo: str, visualizacao: Visualizacao):
    """Atualizar visualização existente"""
    if conteudo_id_mongo not in visualizacoes_fake_db:
        raise HTTPException(status_code=404, detail="Visualização não encontrada")
    visualizacoes_fake_db[conteudo_id_mongo] = visualizacao
    return visualizacao

@router.delete("/{conteudo_id_mongo}")
async def deletar_visualizacao(conteudo_id_mongo: str):
    """Deletar uma visualização"""
    if conteudo_id_mongo not in visualizacoes_fake_db:
        raise HTTPException(status_code=404, detail="Visualização não encontrada")
    del visualizacoes_fake_db[conteudo_id_mongo]
    return {"detail": "Visualização deletada com sucesso"}
