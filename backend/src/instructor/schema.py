from typing import List

from pydantic import BaseModel


class Qualification(BaseModel):
    education: str
    institution: str

    class Config:
        orm_mode = True


class InstructorBase(BaseModel):
    first_name: str
    last_name: str
    pps_number: str
    email: str
    phone: str
    address: str
    eir_code: str
    city: str
    county: str
    country: str
    qualifications: List[Qualification]


class InstructorCreate(InstructorBase):
    pass


class InstructorUpdate(InstructorBase):
    pass


class Instructor(InstructorBase):
    id: int

    class Config:
        orm_mode = True
