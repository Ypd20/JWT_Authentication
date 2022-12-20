from fastapi import FastAPI
from .routes import user, authentication

app = FastAPI()
"""Adding Routes"""
app.include_router(user.router)
app.include_router(authentication.router)
