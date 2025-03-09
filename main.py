from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def blog(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs"}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "All unpublished blogs"}

@app.get('/blog/{id}')
def blogId(id: int):
    return {"data": id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

@app.post('/blog')
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}

@app.get("/blog/{id}/comments")
def comments(limit = 10):
    return limit
    # return {"data": {"1", "2"}}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
