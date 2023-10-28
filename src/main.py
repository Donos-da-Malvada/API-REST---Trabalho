from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Aeronave(BaseModel):
    id: int
    nome: str
    data_entrada: datetime
    data_saida: datetime

# Piazada, vamo adicionar as naves no array.
aeronaves_db = []

@app.post("/aeronaves/", response_model=Aeronave)
def create_aeronave(aeronave: Aeronave):
    aeronave.id = len(aeronaves_db) + 1
    aeronaves_db.append(aeronave)
    return aeronave