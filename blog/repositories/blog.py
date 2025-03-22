from fastapi import status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from typing import List
from .. import oAuth2

def create(request: schemas.Blog, db : Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def getAll(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def getOne(id: int, response: Response, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Details from ID: {id} is not Found"}
    return blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Done"}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return "updated"

