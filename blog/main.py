from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post("/blog")
def blogPost(request: schemas.Blog):
    return request



