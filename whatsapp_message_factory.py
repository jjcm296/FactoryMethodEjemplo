from message_factory import MessageFactory
from whatsapp_message import WhatsAppMessage

class WhatsAppMessageFactory(MessageFactory):
    def create_message(self) -> WhatsAppMessage:
        return WhatsAppMessage()
