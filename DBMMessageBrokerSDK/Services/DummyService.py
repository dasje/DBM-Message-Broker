from DBMMessageBrokerSDK.MessageManagerInterface import MessageManagerInterface
from DBMMessageBrokerSDK.ServiceManagerInterface import ServiceManagerInterface, ServiceInterface
from DBMMessageBrokerSDK.schemas.MessageReceived import MessageReceived

import uuid

class DummyService(ServiceManagerInterface):
    def __init__(self) -> None:
        super().__init__()

    def _create_service(self) -> ServiceInterface:
        class Service(ServiceInterface):
            def __init__(self, service_name: str, service_id: str) -> None:
                super().__init__(service_name, service_id)
        return Service(service_name=self.name, service_id=uuid.uuid4())


    def subscribe_service(self, manager: MessageManagerInterface):
        manager.register_service(self)
    
    def unsubscribe_service(self, manager: MessageManagerInterface):
        manager.deregister_service(self)

    def fetch_message(self, manager: MessageManagerInterface):
        return manager.release_message(self)
    
    async def await_message(self) -> MessageReceived:
        return await super().await_message()