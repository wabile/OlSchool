from sqlalchemy import Column, Integer, String
from src.database.db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    pps_number = Column(String, unique=True)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)
    eir_code = Column(String)
    city = Column(String)
    county = Column(String)
    country = Column(String)
