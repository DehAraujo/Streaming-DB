from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/filmes")
async def buscar_filmes(q: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://s3:8000/buscar?q={q}")
        return response.json()

@app.get("/usuario/{id}")
async def buscar_usuario(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://s2:8000/usuarios/{id}")
        return response.json()

@app.post("/evento")
async def criar_evento(evento: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://s1:8000/evento", json=evento)
        return response.json()
