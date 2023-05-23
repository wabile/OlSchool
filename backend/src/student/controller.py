from fastapi import HTTPException, status

from src.database.db import SessionLocal
from src.student import crud
from src.student.schema import StudentCreate, StudentUpdate


def get_student(student_id: int):
    db = SessionLocal()
    student = crud.get_student(db, student_id)
    db.close()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student


def get_all_students():
    db = SessionLocal()
    students = crud.get_all_students(db)
    db.close()
    return students


def create_student(student: StudentCreate):
    db = SessionLocal()
    db_student = crud.create_student(db, student)
    db.close()
    return db_student


def update_student(student_id: int, student_update: StudentUpdate):
    db = SessionLocal()
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    updated_student = crud.update_student(db, student, student_update)
    db.close()
    return updated_student


def delete_student(student_id: int):
    db = SessionLocal()
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    crud.delete_student(db, student)
    db.close()
    return {"message": "Student deleted"}
