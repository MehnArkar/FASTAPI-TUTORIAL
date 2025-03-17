from typing import Optional
from pydantic import BaseModel
from mangum import Mangum

from fastapi import FastAPI

app = FastAPI()
handler = Mangum(app)


@app.get("/blog")
def index(limit):
    return {"data":f"Bloc List : limit {limit}"}

@app.get("/blog/unpublished")
def unpublished():
    return{"data":"Unpublished blog"}

@app.get("/blog/{id}")
def show(id : int):
    return {"data": id}



@app.get("/blog/{id}/comments")
def comments(id:int):
    return {"data":f"comments of {id}"}


class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post("/blog")
def create_blog(request : Blog):
    return request