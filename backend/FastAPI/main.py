from fastapi import FastAPI
from routers import auth, blogs
from core.database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(blogs.router)
