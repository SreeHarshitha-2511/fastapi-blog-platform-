from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core import security


def get_db_session() -> Session:
    return next(get_db())


get_current_user = security.get_current_user

