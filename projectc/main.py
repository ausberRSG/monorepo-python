"""Module Initial App"""
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """EndPoint to show Hello World"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """Endpoint to show an unique item by id"""
    return {"item_id": item_id, "q": q}
