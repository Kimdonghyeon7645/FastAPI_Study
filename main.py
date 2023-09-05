from fastapi import FastAPI
from database import get_items

app = FastAPI()


@app.get("/")
async def root():
    return get_items()

@app.get("/building")
async def read_building_(q = None):
    return get_items()

