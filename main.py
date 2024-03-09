# Primero importamos FastAPI
from fastapi import FastAPI

# Crear una instancia
app = FastAPI()

# Adicionar informacion de la documantacion
# Titulo
app.title = "My primera APP con FastAPI"
# Version
app.version = "0.0.1"

# inmutable lista de autos
lista_carros = ("Mercedes", "Toyota", "Chevrolet")


@app.get("/", tags=["Home"])
def init():
    return "Hola esta en el home de la APP"


@app.get("/autos", tags=["Autos"])
def obtener_lista_carros():
    return lista_carros
