from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import schemas as user_schema
from ..utilities.schemas import get_db
from ..models import models as user_model
from ..auth.auth import JWTBearer


router = APIRouter(prefix="/user", tags=["Users"])

"""Creating User."""


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user(request: user_schema.CreateUser, db: Session = Depends(get_db)):
    new_user = user_model.User(
        name=request.name, email=request.email, password=request.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


"""Displaying all Users."""


@router.get(
    "/users",
    dependencies=[Depends(JWTBearer())],
    response_model=List[user_schema.ShowUser],
)
def get_users(db: Session = Depends(get_db)):

    users = db.query(user_model.User).all()

    return users
