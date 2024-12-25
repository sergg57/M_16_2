# -*- coding: utf-8 -*-

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

# @app.get("/user/{user_id}")
# async def user(user_id: int=Path(ge=1, le=100, discription='Enter User ID', example='1')) -> str:
#     return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def user(username: str=Path(min_length=5, max_length=20, discription='Enter username',
                example='UrbanUser'), age: int=Path(ge=18, le=120, discription='Enter age',
                example='24')) -> str:
    return  f'Информация о пользователе. Имя: {username}, Возраст {age}'