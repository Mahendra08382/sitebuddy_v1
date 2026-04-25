from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    location: str
    budget: float

class MaterialEntry(BaseModel):
    project_id: int
    material_id: int
    quantity: float
    type: str

class LabourCreate(BaseModel):
    name: str
    role: str
    wage: float

class AttendanceCreate(BaseModel):
    labour_id: int
    project_id: int
    date: str
    status: str