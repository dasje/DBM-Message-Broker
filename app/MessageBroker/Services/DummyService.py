from app.MessageBroker.MessageManager import MessageManagerInterface
from app.MessageBroker.ServiceManager import ServiceManagerInterface
from app.schemas.MessageReceived import MessageReceived

class DummyService(ServiceManagerInterface):
    def __init__(self) -> None:
        super().__init__()

    def subscribe_service(self, manager: MessageManagerInterface):
        manager.register_service(self)
    
    def unsubscribe_service(self, manager: MessageManagerInterface):
        manager.deregister_service(self)

    def fetch_message(self, manager: MessageManagerInterface):
        return manager.release_message(self)
    
    async def await_message(self) -> MessageReceived:
        return await super().await_message()