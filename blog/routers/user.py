from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repositories import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return create(request, db)

@router.get("/", response_model=List[schemas.ShowUserWithBlogs])
def show_all_users(db: Session = Depends(get_db)):
    return show_all(db)

@router.get("/{id}", response_model=schemas.ShowUserWithBlogs)
def show_user(id: int, db: Session = Depends(get_db)):
    return show_user(id, db)