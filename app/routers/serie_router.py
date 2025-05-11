from fastapi import APIRouter, HTTPException
from typing import List
from app.models.serie_model import Serie  # Importando o modelo de dados

router = APIRouter(prefix="/series", tags=["Séries"])

# Banco de dados fake para armazenar as séries
series_fake_db = {}

@router.get("/", response_model=List[Serie])
async def listar_series():
    """Listar todas as séries"""
    return list(series_fake_db.values())

@router.get("/{serie_id}", response_model=Serie)
async def buscar_serie(serie_id: str):
    """Buscar série por ID"""
    serie = series_fake_db.get(serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie

@router.post("/", response_model=Serie)
async def criar_serie(serie: Serie):
    """Criar uma nova série"""
    if serie.titulo in [s.titulo for s in series_fake_db.values()]:
        raise HTTPException(status_code=400, detail="Série já existe")
    series_fake_db[serie.titulo] = serie
    return serie

@router.put("/{serie_id}", response_model=Serie)
async def atualizar_serie(serie_id: str, serie: Serie):
    """Atualizar série existente"""
    if serie_id not in series_fake_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    series_fake_db[serie_id] = serie
    return serie

@router.delete("/{serie_id}")
async def deletar_serie(serie_id: str):
    """Deletar uma série"""
    if serie_id not in series_fake_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    del series_fake_db[serie_id]
    return {"detail": "Série deletada com sucesso"}
