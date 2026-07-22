from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_number = Column(String(30), unique=True, nullable=False)
    caller_name = Column(String(100), nullable=False)
    caller_phone = Column(String(20))
    incident_type = Column(String(100), nullable=False)
    priority = Column(String(20), nullable=False)
    address = Column(String(255), nullable=False)
    description = Column(String(500))
    status = Column(String(30), default="New")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )