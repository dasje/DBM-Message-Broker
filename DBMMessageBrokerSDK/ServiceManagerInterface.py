from abc import abstractmethod, ABCMeta
from typing import List

from DBMMessageBrokerSDK.MessageManagerInterface import MessageManagerInterface
from DBMMessageBrokerSDK.schemas.MessageReceived import MessageReceived
from DBMMessageBrokerSDK.ServiceInterface import ServiceInterface

class ServiceManagerInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, service_name: str) -> None:
        self.name: str = service_name
        self.service: ServiceInterface = self._create_service()

    @abstractmethod
    def create_service(self, manager: MessageManagerInterface) -> ServiceInterface:
        """Create service object."""
        raise NotImplementedError

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
    

    