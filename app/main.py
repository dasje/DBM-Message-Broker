import sentry_sdk
import asyncio
from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
# from starlette.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.api.main import api_router
from app.core.database import sessionmanager
from app.models.ServiceModels import Base
# from app.MessageBroker.MessageManager import MessageManager

def custom_generate_unique_id(route: APIRoute) -> str:
    print(f"{route.tags[0]}-{route.name}")
    return f"{route.tags[0]}-{route.name}"

print("Creating tables")
Base.metadata.create_all(bind=sessionmanager.engine)
print(Base.metadata.tables)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

app.include_router(api_router, prefix=settings.API_V1_STR)

# @app.get("/", tags=["main"])
# def landing():
#     return {"Message": "Hello werld"}