from abc import abstractmethod, ABCMeta
from typing import List
from DBMMessageBrokerSDK.ServiceManagerInterface import ServiceManagerInterface
from DBMMessageBrokerSDK.schemas.Message import Message
from DBMMessageBrokerSDK.schemas.Error import Error, ErrorMessageEnum
from DBMMessageBrokerSDK.schemas.ServiceMessage import ServiceMessage
from DBMMessageBrokerSDK.MessageManagerInterface import MessageManagerInterface
from datetime import date
from app.core.database import sessionmanager    
from app.core.queries.create_service import insert_service as insert_service_query
from app.models.ServiceModels import ServiceModel
import datetime
from DBMMessageBrokerSDK.schemas.RegisterNewService import RegisterNewService

class MessageManager(MessageManagerInterface):
    def __init__(self) -> None:
        super().__init__()

    def create_service(self, new_service: RegisterNewService) -> Message:
        new_service = ServiceModel(
            service_name=new_service.service_name,
            create_date=new_service.request_date
        )
        insert_service_query(new_service)

    def register_service(self, service: ServiceManagerInterface) -> Message:
        try:
            
            if service not in self.services:
                self.services.append(service)
                return Message(message="Service added.")
            else: 
                return Message(message="Service already registered.")
        except Exception as e:
            print(e)
            return Error(message=ErrorMessageEnum.service_not_registered)
        
    def deregister_service(self, service: ServiceManagerInterface) -> Message:
        try:
            if service in self.services:
                self.services.remove(service)
                return Message(message="Service removed.")
            else:
                return Message(message="Service is not registered.")
        except Exception as e:
            print(e)
            return Error(message=ErrorMessageEnum.service_not_deregistered)
        
    async def _notify_services(self, message: ServiceMessage):
        for service in self.services:
            if service.name == message.service_name:
                msg_received = await service.await_message()

    async def release_message(self, service: ServiceManagerInterface) -> ServiceMessage|Error:
        if service not in self.services:
            return Error(message=ErrorMessageEnum.service_not_registered)
        elif service in self.services:
            # Fetch from DB.
            msg = ServiceMessage(
                service_name="dummy_service",
                ttl=100,
                message="Test message",
                sent_date=date.today()
            )
            return msg