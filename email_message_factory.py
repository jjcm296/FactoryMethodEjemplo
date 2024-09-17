from message_factory import MessageFactory
from email_message import EmailMessage

class EmailMessageFactory(MessageFactory):
    def create_message(self) -> EmailMessage:
        return EmailMessage()
    