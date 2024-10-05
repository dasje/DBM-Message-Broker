import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class MessageReceived(SQLModel):
    message: str