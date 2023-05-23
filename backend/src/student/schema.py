from pydantic import BaseModel


class StudentBase(BaseModel):
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


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
