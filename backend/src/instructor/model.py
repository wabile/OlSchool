from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base


class Qualification(Base):
    __tablename__ = "qualifications"

    id = Column(Integer, primary_key=True, index=True)
    education = Column(String)
    institution = Column(String)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))


class Instructor(Base):
    __tablename__ = "instructors"

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
    qualifications = relationship("Qualification", backref="instructor")
