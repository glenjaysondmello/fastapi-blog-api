from fastapi import status, Response, HTTPException, Depends
from .. import schemas, models
from sqlalchemy.orm import Session
from typing import List
from .. import oAuth2

def create(request: schemas.Blog, db : Session, current_user: schemas.User = Depends(oAuth2.get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def getAll(db : Session, current_user: schemas.User = Depends(oAuth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

def getOne(id: int, response: Response, db : Session, current_user: schemas.User = Depends(oAuth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Details from ID: {id} is not Found"}
    return blog

def destroy(id: int, db: Session, current_user: schemas.User = Depends(oAuth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    check_user_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    
    if check_user_blog.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="You are not the owner of this Blog")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"Done"}

def update(id: int, request: schemas.Blog, db: Session, current_user: schemas.User = Depends(oAuth2.get_current_user)):
    check_user_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")

    if check_user_blog.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="You are not the owner of this Blog")

    blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return "updated"

