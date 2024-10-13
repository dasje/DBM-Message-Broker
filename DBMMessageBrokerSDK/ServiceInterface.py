from abc import abstractmethod, ABCMeta
from typing import List

class ServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, service_name: str, service_id: str) -> None:
        self.service_name: str = service_name
        self.service_id: str = service_id
