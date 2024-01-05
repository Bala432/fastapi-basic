from fastapi import FastAPI
from models import Item

app = FastAPI()

@app.get('/')
async def root():
    return {'Home' : ' This is Home Page'}

