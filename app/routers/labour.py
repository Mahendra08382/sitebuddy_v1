from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud

router = APIRouter(prefix="/labour", tags=["Labour"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_labour(labour: schemas.LabourCreate, db: Session = Depends(get_db)):
    return crud.create_labour(db, labour)

@router.post("/attendance")
def attendance(att: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.mark_attendance(db, att)