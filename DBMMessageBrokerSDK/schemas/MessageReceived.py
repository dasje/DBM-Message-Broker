import uuid

from pydantic import EmailStr, BaseModel
from sqlmodel import Field, Relationship, SQLModel

class MessageReceived(BaseModel):
    message: str