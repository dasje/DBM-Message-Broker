import uuid
import enum

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class MessageEnum(str, enum):
    generic_message="Undefined message."

    def __str__(self) -> str:
        return self.value

class Message(SQLModel):
    message: str | MessageEnum