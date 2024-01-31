from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import blog, user
from .routers import authentication

myapp = FastAPI()
models.Base.metadata.create_all(engine)

# necessaire pour tout ce qui est affichage en swagerui
myapp.include_router(authentication.router)
myapp.include_router(blog.router)
myapp.include_router(user.router)







