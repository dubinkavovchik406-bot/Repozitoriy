from fastapi import FastAPI, HTTPException, status
from db import crud

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    user_db = crud.get_user_info(id)
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Пользователь не найден")
    return user_db

@app.get("/users")
def get_users():
    return crud.get_users()