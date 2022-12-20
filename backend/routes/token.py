from datetime import datetime, timedelta
from jose import jwt
from typing import Union, Any

SECRET_KEY = "bff34afdfe57877deed1cd559a2e3b97281b6710069f7fe6303046c94c36ab69"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
""" Creating access token for authentication."""


def create_access_token(subject: Union[str, Any], expire_delta: int = None) -> str:
    if expire_delta is not None:
        expire_delta = datetime.utcnow() + expire_delta
    else:
        expire_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt
