import uuid
from enum import Enum

from pydantic import EmailStr, BaseModel
from sqlmodel import Field, Relationship, SQLModel

class MessageEnum(str, Enum):
    generic_message="Undefined message."

    def __str__(self) -> str:
        return self.value

class Message(BaseModel):
    message: str