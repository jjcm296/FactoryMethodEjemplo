from abc import ABC, abstractmethod
from message import Message

class MessageFactory(ABC):
    @abstractmethod
    def create_message(self) -> Message:
        pass