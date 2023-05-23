from sqlalchemy.orm import Session, joinedload

from src.instructor.model import Instructor, Qualification
from src.instructor.schema import InstructorCreate, InstructorUpdate


def get_instructor(db: Session, instructor_id: int):
    return db.query(Instructor).options(joinedload(Instructor.qualifications)).filter(Instructor.id == instructor_id).first()


def get_all_instructors(db: Session):
    return db.query(Instructor).options(joinedload(Instructor.qualifications)).all()


def create_instructor(db: Session, instructor: InstructorCreate):
    qualifications = []
    for qualification in instructor.qualifications:
        qualifications.append(Qualification(**qualification.dict()))
    db_instructor = Instructor(
        first_name=instructor.first_name,
        last_name=instructor.last_name,
        pps_number=instructor.pps_number,
        email=instructor.email,
        phone=instructor.phone,
        address=instructor.address,
        eir_code=instructor.eir_code,
        city=instructor.city,
        county=instructor.county,
        country=instructor.country,
        qualifications=qualifications
    )
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return get_instructor(db, db_instructor.id)


def update_instructor(db: Session, instructor: Instructor, instructor_update: InstructorUpdate):  # NoQa
    db.query(Qualification).filter(Qualification.instructor_id == instructor.id).delete()
    db.commit()
    for field, value in instructor_update.dict(exclude={"qualifications"}).items():
        setattr(instructor, field, value)
    qualifications = []
    for qualification in instructor_update.qualifications:
        qualifications.append(Qualification(**qualification.dict()))
    print(qualifications)
    instructor.qualifications = qualifications
    # db.add_all(qualifications)
    db.add(instructor)
    db.commit()
    db.refresh(instructor)
    return instructor


def delete_instructor(db: Session, instructor: Instructor):
    db.delete(instructor)
    db.commit()
