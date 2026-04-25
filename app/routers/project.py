from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)