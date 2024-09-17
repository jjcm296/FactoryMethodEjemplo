import pywhatkit as kit
from message import Message
import datetime

class WhatsAppMessage(Message):
    def send(self, recipient: str, content: str):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 2  # Enviar dentro de 2 minutos

        # Envía el mensaje de WhatsApp usando pywhatkit
        kit.sendwhatmsg(recipient, content, hour, minute)
        print(f"Mensaje WhatsApp enviado a {recipient} a las {hour}:{minute}")
