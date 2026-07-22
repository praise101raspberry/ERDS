from datetime import datetime

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.incident import Incident
from app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentUpdate,
)

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)

@router.put("/{incident_id}")
def update_incident(
    incident_id: int,
    updated: IncidentUpdate
):
    db = SessionLocal()

    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    incident.priority = updated.priority
    incident.status = updated.status
    incident.caller_name = updated.caller_name
    incident.caller_phone = updated.caller_phone
    incident.address = updated.address
    incident.description = updated.description

    db.commit()
    db.refresh(incident)

    return incident


@router.post("/", response_model=IncidentResponse)
def create_incident(data: IncidentCreate):

    db: Session = SessionLocal()

    incident = Incident(
        incident_number=f"INC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        caller_name=data.caller_name,
        caller_phone=data.caller_phone,
        incident_type=data.incident_type,
        priority=data.priority,
        address=data.address,
        description=data.description,
        status="New",
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


@router.get("/", response_model=list[IncidentResponse])
def get_incidents():

    db: Session = SessionLocal()

    return db.query(Incident).all()


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: int):

    db: Session = SessionLocal()

    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident