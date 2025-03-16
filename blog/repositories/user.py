from fastapi import status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_all(db: Session):
    users = db.query(models.User).all()
    return users

def show_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Details from ID: {id} is not Found")
    return user