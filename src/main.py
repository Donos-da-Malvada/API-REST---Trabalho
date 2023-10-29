from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json


app = FastAPI()

class Aeronave(BaseModel):    

    id: int = 0
    nome: str
    data_entrada: datetime = datetime.now()
    data_saida: datetime = None


aeronaves_db = []


@app.get("/aeronaves/listar", response_model=aeronaves_db)
def listar_aeronaves():    
    return list(filter(lambda aeronave: aeronave.data_saida is None, aeronaves_db))

@app.post("/aeronaves/", response_model=Aeronave)
def create_aeronave(aeronave: Aeronave):
    if next((a for a in aeronaves_db if a.data_saida is None and a.nome == aeronave.nome), None):
        raise HTTPException(status_code=400, detail="Aeronave já registrada")

    aeronave.id = len(aeronaves_db) + 1
    aeronave.data_saida = None
    aeronaves_db.append(aeronave)
    return aeronave

@app.patch("/aeronaves/{nome}/partida", response_model=Aeronave)
async def atualizar_aeronave(nome: str):
    for registro in list(filter(lambda aeronave: aeronave.data_saida is None, aeronaves_db)):
        if registro.data_saida == None and registro.nome == nome:
            registro.data_saida = datetime.now()
            return registro

    raise HTTPException(status_code=404, detail="Aeronave não encontrada")


@app.delete("/aeronaves/{nome}/deletar")
def delete_aeronave(nome: str):
    for registro in list(filter(lambda aeronave: aeronave.data_saida is None, aeronaves_db)):
        if registro.data_saida == None and registro.nome == nome:
            aeronaves_db.remove(registro)
            return {"message": "Aeronave removida com sucesso"}

    raise HTTPException(status_code=404, detail="Aeronave não encontrada")
