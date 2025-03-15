from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()
get_db = database.get_db

@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def blogPost(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog", response_model=List[schemas.ShowBlog], tags=["Blogs"])
def all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blogs"])
def show(id: int, response: Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Details from ID: {id} is not Found"}
    return blog

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Done"}

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return "updated"

