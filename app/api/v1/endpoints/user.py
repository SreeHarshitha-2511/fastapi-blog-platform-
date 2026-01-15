from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import User, ShowUser
from app.core.database import get_db
from app.repositories import user as user_repository


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user_repository.create(request, db)


@router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_repository.show(id, db)

