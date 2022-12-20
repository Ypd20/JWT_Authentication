from pydantic import BaseModel
from datetime import date
from typing import Optional

"""User model"""
class User(BaseModel):
    name : str
    email : str
    gender : str
    created_at : date
    updated_at : date
    is_active : bool
    is_deleted : bool


"""Create user response model"""
class CreateUser(BaseModel):
    name : str
    email : str
    password : str

    class Config:
        orm_mode = True


"""Show User response model"""
class ShowUser(BaseModel):
    name: str
    email : str

    class Config:
        orm_mode = True


"""Login response model"""
class Login(BaseModel):
    name : str
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    name: Optional[str] = None

  
