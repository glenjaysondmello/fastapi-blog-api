from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repositories import auth

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

get_db = database.get_db

@router.post("/")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    return auth.login(request, db)