# 🚀 Trabajo Práctico 3 - API REST con Docker y Versionamiento

Este repositorio contiene el Trabajo Práctico 3 de la materia MLOps. El objetivo fue construir una API utilizando **FastAPI**, aplicar versionamiento de código con múltiples ramas, y realizar la conteinerización del proyecto con **Docker**.

## 🧱 Descripción

- La API expone dos endpoints para manejar usuarios.
- Se utilizó FastAPI junto a Pydantic para la validación de datos.
- El proyecto fue conteinerizado con Docker y la imagen se subió a DockerHub.
- Se aplicó versionamiento mediante las ramas `main`, `develop`, `staging` y `feature`.

## 📁 Estructura

- `main.py`: Código principal de la API.
- `app/models.py`: Modelo de datos del usuario.
- `requirements.txt`: Dependencias del proyecto.
- `Dockerfile`: Archivo de configuración para crear la imagen Docker.
- `README.md`: Este archivo.

## 🔧 Instrucciones para ejecutar localmente

### 1. Clonar el repositorio

git clone [https://github.com/Jasser710/tu-repo.git](https://github.com/Jasser710/Trabajo-practico-3.git)

cd Trabajo-practico-3

### 2. Crear y activar un entorno virtual

python -m venv venv

# Activar:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

### 3. Instalar las dependencias

pip install -r requirements.txt

### 4. Ejecutar el servidor localmente

uvicorn app.main:app --reload

Abrir en el navegador:

http://127.0.0.1:8000/docs

## 🐳 Instrucciones para correr con Docker

### 1. Crear la imagen

docker build -t jasserpalacios/trabajo-practico-3 .

### 2. Ejecutar el contenedor

docker run -p 8000:8000 jasserpalacios/trabajo-practico-3

Luego abrir en el navegador:

http://localhost:8000/docs

## 📦 Imagen Docker publicada

La imagen está disponible en DockerHub:

[[https://hub.docker.com/r/Jasser710/api-usuarios](https://hub.docker.com/r/jasserpalacios/trabajo-practico-3)](https://hub.docker.com/r/jasserpalacios/trabajo-practico-3
)

## ✍️ Autor

- Nombre: Jasser Palacios
- GitHub: https://github.com/Jasser710
