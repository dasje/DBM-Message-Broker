from sqlalchemy import insert
from app.models.ServiceModels import ServiceModel
from app.core.database import sessionmanager

def insert_service(service: ServiceModel):
    session = sessionmanager.get_db()
    session = next(session)
    print("Inserting data", service)
    session.add(service)
    session.commit()