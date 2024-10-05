import uuid
import enum
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class ErrorMessageEnum(str, enum):
    generic_error="Undefined error."
    service_not_registered = "Could not register service."
    service_not_deregistered = "Could not deregister service."

    def __str__(self) -> str:
        return self.value

class Error(SQLModel):
    message: ErrorMessageEnum