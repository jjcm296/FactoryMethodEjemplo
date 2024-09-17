from message_factory import MessageFactory
from sms_message import SmsMessage

class SmsMessageFactory(MessageFactory):
    def create_message(self) -> SmsMessage:
        return SmsMessage()