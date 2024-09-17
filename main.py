from sms_message_factory import SmsMessageFactory
from whatsapp_message_factory import WhatsAppMessageFactory
from email_message_factory import EmailMessageFactory

def main():
    message_type = 'sms'
    recipient = '+529221860109'
    content = 'magdielito.com'

    if message_type == 'sms':
        factory = SmsMessageFactory()
    elif message_type == 'whatsapp':
        factory = WhatsAppMessageFactory()
    elif message_type == 'email':
        factory = EmailMessageFactory()
    else:
        raise ValueError("Tipo de mensaje no soportado")

    message = factory.create_message()
    message.send(recipient, content)

if __name__ == "__main__":
    main()
