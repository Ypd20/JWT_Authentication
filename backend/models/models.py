from sqlalchemy import Column, INTEGER, String, BOOLEAN, DATETIME, Date
from ..database.database import Base
from datetime import datetime

""" Database Model for User table. """


class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(BOOLEAN, default=True)
    is_deleted = Column(BOOLEAN, default=False)
    created_at = Column(DATETIME, default=datetime.utcnow)
    updated_at = Column(DATETIME, default=datetime.utcnow)
