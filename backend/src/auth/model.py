from sqlalchemy import Column, Integer, String
from src.database.db import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

