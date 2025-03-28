from fastapi import status, Response, HTTPException, Depends
from .. import schemas, models, JWTtoken
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import Hash
from typing import Annotated


def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")

