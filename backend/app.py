from fastapi import FastAPI
from .routes import login, signup

app = FastAPI()
"""Adding Routes"""
app.include_router(signup.router)
app.include_router(login.router)
