from abc import abstractmethod, ABCMeta
from typing import List
from app.MessageBroker.ServiceManager import ServiceManagerInterface
from app.schemas.Message import Message
from app.schemas.Error import Error, ErrorMessageEnum
from app.schemas.ServiceMessage import ServiceMessage
import asyncio
from datetime import date

class MessageManagerInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        self.services: List[ServiceManagerInterface] = []

    @abstractmethod
    def register_service(self, service: ServiceManagerInterface) -> Message:
        """Register a new service."""
        raise NotImplementedError
    
    @abstractmethod
    def deregister_service(self, service: ServiceManagerInterface) -> Message:
        """Deregister a service."""
        raise NotImplementedError
    
    @abstractmethod
    async def _notify_services(self, message: ServiceMessage):
        """Notify all services with service name in message."""
        raise NotImplementedError
    
    @abstractmethod
    async def release_message(self, service: ServiceManagerInterface) -> ServiceMessage:
        """Validate service, fetch message from db and post to service."""
        raise NotImplementedError
    

class MessageManager(MessageManagerInterface):
    def __init__(self) -> None:
        super().__init__()

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