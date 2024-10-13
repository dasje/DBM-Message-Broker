import uuid
import enum

from datetime import date
from pydantic import EmailStr, BaseModel
from sqlmodel import Field, Relationship, SQLModel

class RegisterNewService(BaseModel):
    service_name: str
    request_date: date

class RegisterNewServiceResponse(BaseModel):
    service_name: str

class RegisterNewServiceResponseSuccess(RegisterNewServiceResponse):
    service_id: str

class RegisterNewServiceResponseError(RegisterNewServiceResponse):
    message: str