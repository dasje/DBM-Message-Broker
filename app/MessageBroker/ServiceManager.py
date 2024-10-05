from abc import abstractmethod, ABCMeta
from typing import List

from app.MessageBroker.MessageManager import MessageManagerInterface
from app.schemas.MessageReceived import MessageReceived

class ServiceManagerInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, service_name: str) -> None:
        self.name: str = service_name

    @abstractmethod
    def subscribe_service(self, manager: MessageManagerInterface):
        """Register a new service."""
        raise NotImplementedError
    
    @abstractmethod
    def unsubscribe_service(self, manager: MessageManagerInterface):
        """Deregister a service."""
        raise NotImplementedError
    
    @abstractmethod
    def fetch_message(self, manager: MessageManagerInterface):
        """Fetch message from manager service."""
        raise NotImplementedError
    
    @abstractmethod
    async def await_message(self) -> MessageReceived:
        """Await message from manager."""
        raise NotImplementedError
    

    