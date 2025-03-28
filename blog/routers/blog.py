from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repositories import blog
from typing import List
from .. import oAuth2

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.create(request, db, current_user)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.getAll(db, current_user)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db : Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.getOne(id, response, db, current_user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.destroy(id, db, current_user)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blog.update(id, request, db, current_user)

