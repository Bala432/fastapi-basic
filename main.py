from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message" : "This is Home Page"}

@app.get("/home/{feature_name}")
async def get_feature(feature_name: str):
    return {'feature' : feature_name}