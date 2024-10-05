import uuid
import enum

from datetime import date
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class ServiceMessage(SQLModel):
    service_name: str
    ttl: int
    message: str
    sent_date: date