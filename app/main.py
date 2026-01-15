from fastapi import FastAPI

from app.core.database import Base, engine
from app import models
from app.api.v1.endpoints import auth, blog, user


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)
