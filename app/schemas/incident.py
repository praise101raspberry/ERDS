from pydantic import BaseModel


class IncidentCreate(BaseModel):
    caller_name: str
    caller_phone: str
    incident_type: str
    priority: str
    address: str
    description: str


class IncidentUpdate(BaseModel):
    priority: str
    status: str
    caller_name: str
    caller_phone: str
    address: str
    description: str


class IncidentResponse(IncidentCreate):
    id: int
    incident_number: str
    status: str

    class Config:
        from_attributes = True

