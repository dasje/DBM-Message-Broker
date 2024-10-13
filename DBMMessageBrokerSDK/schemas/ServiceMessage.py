import uuid
import enum

from datetime import date
from pydantic import EmailStr, BaseModel
from sqlmodel import Field, Relationship, SQLModel

class ServiceMessage(BaseModel):
    service_name: str
    service_contact: str
    ttl: int
    message: str
    sent_date: date