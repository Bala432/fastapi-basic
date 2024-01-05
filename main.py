from fastapi import FastAPI, Path
from models import Item
from typing import Annotated

app = FastAPI()

@app.get('/')
async def root():
    return {'Home' : ' This is Home Page'}

@app.post('/items')
async def post(item: Item):
    if item.tax is not None:
        item.price = item.price + (item.price * item.tax) / 100
    
    return {"Item" : item}

@app.get('/items/{item_id}')
async def get(item_id: Annotated[int,Path( title = "Get Item ID", ge=3)]):
    return { 'Item' : item_id}
