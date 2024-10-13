from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

# from app.api.deps import get_current_active_superuser
from app.MessageBroker.MessageManager import MessageManagerInterface
from DBMMessageBrokerSDK.schemas.Message import Message
from DBMMessageBrokerSDK.schemas.RegisterNewService import RegisterNewService, RegisterNewServiceResponseError, RegisterNewServiceResponseSuccess

from app.core.database import sessionmanager
from app import MessageBroker


router = APIRouter()

@router.post(
    "/register",
    # dependencies=[Depends()],
    status_code=201,
)
def register_new_service(msg: RegisterNewService) -> RegisterNewServiceResponseSuccess | RegisterNewServiceResponseError:
    """
    Test.
    """
    # Execute logic
    print(msg)
    MessageBroker.create_service(msg)
    return RegisterNewServiceResponseSuccess(service_id="newId", service_name=msg.service_name)


@router.get("/health-check/")
def health_check() -> bool:
    return True