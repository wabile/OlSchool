from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.jwt import decode_access_token, get_user
from src.database.db import get_db
from src.student import controller, schema
from src.student.schema import Student

student_router = APIRouter()


@student_router.get("/", response_model=List[Student])
def get_all_students(user: dict = Depends(get_user)):
    students = controller.get_all_students()
    return students


@student_router.get("/{student_id}")
def get_student(student_id: int, user: dict = Depends(get_user)):
    student = controller.get_student(student_id)
    return student


@student_router.post("/")
def create_student(student: schema.StudentCreate, user: dict = Depends(get_user)):
    created_student = controller.create_student(student)
    return created_student


@student_router.put("/{student_id}")
def update_student(student_id: int, student_update: schema.StudentUpdate, user: dict = Depends(get_user)):
    updated_student = controller.update_student(student_id, student_update)
    return updated_student


@student_router.delete("/{student_id}")
def delete_student(student_id: int, user: dict = Depends(get_user)):
    response = controller.delete_student(student_id)
    return response
