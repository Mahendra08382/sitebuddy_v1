from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    budget = Column(Float)

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(String)

class MaterialTransaction(Base):
    __tablename__ = "material_transactions"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    quantity = Column(Float)
    type = Column(String)  # RECEIVED / USED

class Labour(Base):
    __tablename__ = "labour"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    wage = Column(Float)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    labour_id = Column(Integer, ForeignKey("labour.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(Date)
    status = Column(String)