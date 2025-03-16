from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repositories import blog
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def blogPost(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    return blog.getAll(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db : Session = Depends(get_db)):
    return blog.getOne(id, response, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

