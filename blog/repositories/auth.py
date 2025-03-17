from fastapi import status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    return user