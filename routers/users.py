from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Inicia el server: uvicorn users:app --reload


#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Braian", surname="Missouri", url="https://Missouri.dev", age=25),
    User(id=2, name="Kevin", surname="Devian", url="https://KevinDevian.com", age=35),
    User(id=3, name="Braian", surname="Dan", url="https://Braian.com", age=40)
]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Braian", "url": "https://Missouri.dev", "age": 25},
            {"name": "Moure", "surname": "Devian", "url": "https://KevinDevian.com", "age": 35},
            {"name": "Haakon", "surname": "Dan", "url": "https://Braian.com", "age": 40}]


@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")  # Path
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query
async def user(id: int):
    return search_user(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No se ha eliminado el usuario")
    return {"message": "Usuario eliminado correctamente"}   



def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}