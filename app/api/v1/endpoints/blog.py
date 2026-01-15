from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.blog import Blog, ShowBlog
from app.schemas.user import User
from app.api.v1.dependencies import get_current_user
from app.core.database import get_db
from app.repositories import blog as blog_repository


router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.get("/", response_model=List[ShowBlog])
def all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog_repository.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog_repository.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog_repository.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog_repository.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=ShowBlog)
def show(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog_repository.show(id, db)

