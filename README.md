# Python Backend FastAPI

Curso y proyecto backend desarrollado con FastAPI y MongoDB.

## 🚀 Características

- API RESTful con **FastAPI**.
- Base de datos NoSQL con **MongoDB** (PyMongo).
- Autenticación básica y mediante **JWT (JSON Web Tokens)** y **OAuth2**.
- Hashing y seguridad de contraseñas con **Passlib** / **Bcrypt**.
- Servidor de archivos estáticos (`/static`).
- Documentación interactiva automática con Swagger UI (`/docs`) y ReDoc (`/redoc`).

## 🛠️ Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/emmardi76/PythonBackendFastAPI.git
   cd PythonBackendFastAPI
   ```

2. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   Copiar `.env.example` a `.env` y configurar las variables necesarias:
   ```bash
   cp .env.example .env
   ```

5. Ejecutar la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

## 📚 Documentación de la API

Una vez en ejecución, puedes acceder a:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

