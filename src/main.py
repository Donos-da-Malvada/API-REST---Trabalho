from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Aeronave(BaseModel):    

    id: int = 0
    nome: str
    data_entrada: datetime = datetime.now()
    data_saida: datetime = None


aeronaves_db = []


@app.get("/aeronaves/listar", response_model=aeronaves_db)
def listar_aeronaves():    
    return list(filter(lambda aeronave: aeronave.data_saida != None, aeronaves_db))

@app.post("/aeronaves/", response_model=Aeronave)
def create_aeronave(aeronave: Aeronave):
    aeronave.id = len(aeronaves_db) + 1
    aeronave.data_saida = None
    aeronaves_db.append(aeronave)
    return aeronave


