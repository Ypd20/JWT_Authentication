from pydantic import BaseModel
from datetime import date
from typing import Optional


class User(BaseModel):
    name: str
    email: str
    gender: str
    created_at: date
    updated_at: date
    is_active: bool
    is_deleted: bool


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    name: Optional[str] = None

    class Config:
        orm_mode = True
