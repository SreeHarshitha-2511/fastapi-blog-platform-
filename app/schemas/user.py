from __future__ import annotations

from typing import TYPE_CHECKING, List

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas.blog import Blog


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True

