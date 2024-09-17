from twilio.rest import Client
from message import Message
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

class SmsMessage(Message):
    def send(self, recipient: str, content: str):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=content,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient
        )
        print(f"Mensaje SMS enviado...: {message.sid}")
