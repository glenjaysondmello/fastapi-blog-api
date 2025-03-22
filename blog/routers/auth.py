from fastapi import APIRouter, Depends, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repositories import auth
from typing import Annotated

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

get_db = database.get_db

@router.post("/")
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    return auth.login(request, db)