# app/router/avaliacao_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.avaliacao_model import Avaliacao

router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])

# Simulação de banco de dados usando conteudo_id_mongo como chave
avaliacoes_fake_db = {}

@router.get("/", response_model=List[Avaliacao])
async def listar_avaliacoes():
    return list(avaliacoes_fake_db.values())

@router.get("/{conteudo_id_mongo}", response_model=Avaliacao)
async def buscar_avaliacao(conteudo_id_mongo: str):
    avaliacao = avaliacoes_fake_db.get(conteudo_id_mongo)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao

@router.post("/", response_model=Avaliacao)
async def criar_avaliacao(avaliacao: Avaliacao):
    if avaliacao.conteudo_id_mongo in avaliacoes_fake_db:
        raise HTTPException(status_code=400, detail="Avaliação já existe para esse conteúdo")
    avaliacoes_fake_db[avaliacao.conteudo_id_mongo] = avaliacao
    return avaliacao

@router.put("/{conteudo_id_mongo}", response_model=Avaliacao)
async def atualizar_avaliacao(conteudo_id_mongo: str, avaliacao: Avaliacao):
    if conteudo_id_mongo not in avaliacoes_fake_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    avaliacoes_fake_db[conteudo_id_mongo] = avaliacao
    return avaliacao

@router.delete("/{conteudo_id_mongo}")
async def deletar_avaliacao(conteudo_id_mongo: str):
    if conteudo_id_mongo not in avaliacoes_fake_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    del avaliacoes_fake_db[conteudo_id_mongo]
    return {"detail": "Avaliação deletada com sucesso"}
