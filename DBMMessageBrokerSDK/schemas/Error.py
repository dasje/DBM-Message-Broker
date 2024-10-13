from enum import StrEnum
from pydantic import BaseModel

class ErrorMessageEnum(StrEnum):
    generic_error="Undefined error."
    service_not_registered = "Could not register service."
    service_not_deregistered = "Could not deregister service."

    def __str__(self) -> str:
        return self.value

class Error(BaseModel):
    message: ErrorMessageEnum