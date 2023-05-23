from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.jwt import decode_access_token, get_user
from src.database.db import get_db
from src.instructor import controller, schema

instructor_router = APIRouter()


@instructor_router.get("/", response_model=List[schema.Instructor])
def get_all_instructors(user: dict = Depends(get_user)):
    instructors = controller.get_all_instructors()
    return instructors


@instructor_router.get("/{instructor_id}", response_model=schema.Instructor)
def get_instructor(instructor_id: int, user: dict = Depends(get_user)):
    instructor = controller.get_instructor(instructor_id)
    return instructor


@instructor_router.post("/", response_model=schema.Instructor)
def create_instructor(instructor: schema.InstructorCreate, user: dict = Depends(get_user)):
    created_instructor = controller.create_instructor(instructor)
    return created_instructor


@instructor_router.put("/{instructor_id}", response_model=schema.Instructor)
def update_instructor(
        instructor_id: int,
        instructor_update: schema.InstructorUpdate,
        user: dict = Depends(get_user)
):
    updated_instructor = controller.update_instructor(instructor_id, instructor_update)
    return updated_instructor


@instructor_router.delete("/{instructor_id}")
def delete_instructor(instructor_id: int, user: dict = Depends(get_user)):
    response = controller.delete_instructor(instructor_id)
    return response
