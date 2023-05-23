from sqlalchemy.orm import Session
from src.student.model import Student
from src.student.schema import StudentCreate, StudentUpdate


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def get_all_students(db: Session):
    return db.query(Student).all()


def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student: Student, student_update: StudentUpdate):
    for field, value in student_update.dict().items():
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student: Student):
    db.delete(student)
    db.commit()
