from fastapi import FastAPI
from .database import engine, Base
from .routers import project, material, labour

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Site Buddy API")

app.include_router(project.router)
app.include_router(material.router)
app.include_router(labour.router)

@app.get("/") 
def root():
    return {"message": "Site Buddy API running"}