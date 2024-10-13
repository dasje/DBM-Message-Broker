from abc import abstractmethod, ABCMeta
from typing import List

from DBMMessageBrokerSDK.ServiceInterface import ServiceInterface
from DBMMessageBrokerSDK.schemas.Message import Message
from DBMMessageBrokerSDK.schemas.ServiceMessage import ServiceMessage

class MessageManagerInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        self.services: List[ServiceInterface] = []

    @abstractmethod
    def create_service(self, service_name: ServiceInterface) -> Message:
        """Create a new service."""
        raise NotImplementedError

    @abstractmethod
    def register_service(self, service: ServiceInterface) -> Message:
        """Register a new service."""
        raise NotImplementedError
    
    @abstractmethod
    def deregister_service(self, service: ServiceInterface) -> Message:
        """Deregister a service."""
        raise NotImplementedError
    
    @abstractmethod
    async def _notify_services(self, message: ServiceMessage):
        """Notify all services with service name in message."""
        raise NotImplementedError
    
    @abstractmethod
    async def release_message(self, service: ServiceInterface) -> ServiceMessage:
        """Validate service, fetch message from db and post to service."""
        raise NotImplementedError