from fastapi import FastAPI
from db import engine
import models
from routers import project, update, bullet, user, authentication
from fastapi_pagination import add_pagination

app =  FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(project.router)
app.include_router(update.router)
app.include_router(bullet.router)
app.include_router(user.router)
app.include_router(authentication.router)

add_pagination(app)