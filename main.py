
# documentación oficial: https://fastapi.tiangolo.com/es

# Instala FastApi: pip install "fastapi[all]"
from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db  
from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Url local:
# http://127.0.0.1:8000/
# Documentación automática:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

@app.get("/")
async def root():
    return {"message": "Hola desde FastAPI"}

@app.get("/HomePage")
async def HomePage():
    return {"HomePage": "https://apipeliculasnet8azdeploy-gpbub8grbbfab4ef.centralus-01.azurewebsites.net/"}

# Access any image: http://localhost:8000/imagenes/python.jpg
# return FileResponse("imagenes/python.jpg", media_type="image/png")
