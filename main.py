# Primero importamos FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Crear una instancia
app = FastAPI()

# Adicionar informacion de la documantacion
# Titulo
app.title = "My primera APP con FastAPI"
# Version
app.version = "0.0.1"

# inmutable lista de autos
lista_carros = [
    {"brand": "Ford", "model": "Mustang", "year": 1964},
    {"brand": "Mercedes", "model": "AS", "year": 1954},
    {"brand": "Toyota", "model": "TXT", "year": 1934},
    {"brand": "Chevrolet", "model": "Aveo", "year": 2034},
]


@app.get("/", tags=["Home"])
def home():
    return HTMLResponse('<h1>Hola esta en el home de la APP</h1>')


@app.get("/autos", tags=["Autos"])
def obtener_lista_carros():
    return lista_carros
