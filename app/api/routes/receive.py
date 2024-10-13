from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

# from app.api.deps import get_current_active_superuser
from DBMMessageBrokerSDK.schemas.Message import Message
from DBMMessageBrokerSDK.schemas.ServiceMessage import ServiceMessage

router = APIRouter()

@router.post(
    "/",
    # dependencies=[Depends()],
    status_code=201,
)
def receive_message(msg: ServiceMessage) -> Message:
    """
    Test.
    """
    # Execute logic
    print(msg)
    return Message(message=f"Sending message to {msg.service_contact}")


@router.get("/health-check/")
async def health_check() -> bool:
    return True