from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User
from app.api.v1.router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Emergency Response and Dispatch System",
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "Welcome to ERDS API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
    