from fastapi import HTTPException, status

from src.database.db import SessionLocal
from src.instructor import crud
from src.instructor.schema import InstructorCreate, InstructorUpdate


def get_instructor(instructor_id: int):
    db = SessionLocal()
    instructor = crud.get_instructor(db, instructor_id)
    db.close()
    if not instructor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instructor not found")
    return instructor


def get_all_instructors():
    db = SessionLocal()
    instructors = crud.get_all_instructors(db)
    db.close()
    return instructors


def create_instructor(instructor: InstructorCreate):
    db = SessionLocal()
    db_instructor = crud.create_instructor(db, instructor)
    db.close()
    return db_instructor


def update_instructor(instructor_id: int, instructor_update: InstructorUpdate):
    db = SessionLocal()
    instructor = crud.get_instructor(db, instructor_id)
    if not instructor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instructor not found")
    updated_instructor = crud.update_instructor(db, instructor, instructor_update)
    db.close()
    return updated_instructor


def delete_instructor(instructor_id: int):
    db = SessionLocal()
    instructor = crud.get_instructor(db, instructor_id)
    if not instructor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instructor not found")
    crud.delete_instructor(db, instructor)
    db.close()
    return {"message": "Instructor deleted"}
