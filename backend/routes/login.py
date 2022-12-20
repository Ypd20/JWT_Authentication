from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import schemas as login_schema
from ..utilities.schemas import get_db
from sqlalchemy.orm import Session
from ..models import models
from .tokens import create_access_token


router = APIRouter(tags=["Login"])

"""User Login"""
@router.post("/login")
def login(request: login_schema.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == request.name).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect Username"
        )

    pwd = db.query(models.User).filter(models.User.password == request.password).first()
    if not pwd:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect Password"
        )

    access_token = create_access_token(models.User.name)
    return {"access_token": access_token, "token_type": "bearer"}
