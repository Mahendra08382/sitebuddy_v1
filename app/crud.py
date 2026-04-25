from sqlalchemy.orm import Session
from . import models, schemas

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(
        name=project.name,
        location=project.location,
        budget=project.budget
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def create_material_entry(db: Session, entry: schemas.MaterialEntry):
    db_entry = models.MaterialTransaction(**entry.dict())
    db.add(db_entry)
    db.commit()
    return db_entry


def create_labour(db: Session, labour: schemas.LabourCreate):
    db_labour = models.Labour(**labour.dict())
    db.add(db_labour)
    db.commit()
    return db_labour


def mark_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_att = models.Attendance(**attendance.dict())
    db.add(db_att)
    db.commit()
    return db_att