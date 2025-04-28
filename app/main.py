from fastapi import FastAPI
from app.models import Usuario

app = FastAPI()

# Lista que simula una base de datos
usuarios = []

@app.post("/user")
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensaje": "Usuario guardado correctamente"}

@app.get("/user")
def obtener_usuarios():
    return usuarios

