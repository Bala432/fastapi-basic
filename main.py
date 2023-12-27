from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role
from typing import List

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),first_name='Thomas',last_name='Shelby',gender=Gender.male,roles=[Role.admin,Role.user]),
    User(id=uuid4(),first_name='Grace',last_name='Burgess',gender=Gender.female,roles=[Role.user])
]   

@app.get("/")
async def home():
    return {"message" : "This is Home Page"}

@app.get("/home/{feature_name}")
async def get_feature(feature_name: str):
    return {'feature' : feature_name}

@app.get('/users/list')
async def get_users_list():
    return db