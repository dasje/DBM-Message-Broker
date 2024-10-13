
from sqlalchemy import Column, Integer, String, Date
# from app.models import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ServiceMessageModel(Base):
    __tablename__ = "service_message"

    id = Column(Integer, primary_key=True)
    service_name = Column(String)
    service_contact = Column(String)
    ttl = Column(Integer)
    message = Column(String)
    sent_date = Column(Date)

class ServiceModel(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String)
    create_date = Column(Date)