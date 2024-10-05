from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from app.api.deps import get_current_active_superuser
from app.models import Message

router = APIRouter()


@router.post(
    "/test/",
    dependencies=[Depends()],
    status_code=201,
)
def test(var: str) -> Message:
    """
    Test.
    """
    # Execute logic
    return Message(message="Test completed")


@router.get("/health-check/")
async def health_check() -> bool:
    return True