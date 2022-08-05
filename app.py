from datetime import datetime
from fastapi import FastAPI, HTTPException
from typing import Text, Optional
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI()

balones = []

# Modelo de Balones
class Balon(BaseModel):
    id: Optional[str]
    precio: int
    fabricante: str
    detalles: str
    inflado: bool = False


@app.get('/')
def read_root():
    return {"Mensaje": "Bienvenido a mi Fabrica de balones"}

@app.get('/balones')
def obtener_balones():
    return balones


@app.post('/balones')
def guardar_balon(balon: Balon):
    balon.id = str(uuid())
    balones.append(balon.dict())
    return balones[-1]

@app.get('/balones/{balon_id}')
def obtener_balon(balon_id: str):
    print(balon_id)
    for balon in balones:
        if balon["id"] == balon_id:
            return balon
    raise HTTPException(status_code=404, detail="Balon no encontrado")


@app.delete('/balones/{balon_id}')
def eliminar_balon(balon_id: str):
    for indice, balon in enumerate(balones):
        if balon["id"] == balon_id:
            balones.pop(indice)
            return{"Mensaje:" "Balon eliminado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Balon no encontrado")


@app.put('/balones/{balon_id}')
def update_post(balon_id: str, BalonActualizado: Balon):
    for indice, balon in enumerate(balones):
        if balon["id"] == balon_id:
            balones[indice]["precio"] = BalonActualizado.precio
            balones[indice]["fabricante"] = BalonActualizado.fabricante
            balones[indice]["detalles"] = BalonActualizado.detalles
            return {"Mensaje": "Balon actualizado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Balon no encontrado")