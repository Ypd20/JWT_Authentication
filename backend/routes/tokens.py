from datetime import datetime, timedelta
from jose import jwt
from typing import Union, Any

"""SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES"""
SECRET_KEY = "b'a49ddcd974107e238153eaf0e59aeb65da74ffb0d4ed98ea'"
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
        """Encoding the data"""
    to_encode = {"exp": expire_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

    
"""Decoding the data"""
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return decoded_token
    except:
        return {}
