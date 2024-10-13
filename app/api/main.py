from fastapi import APIRouter, Depends

from app.api.routes import utils, receive,service

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(receive.router, prefix="/receive", tags=["receive"])
api_router.include_router(service.router, prefix="/service", tags=["service"])