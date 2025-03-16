from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[schemas.ShowUserWithBlogs])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.ShowUserWithBlogs)
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    return user