import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

EMAIL_CONFIG = {
    'host' : 'smtp.gmail.com',
    'port': 465,
    'username': 'abelsonmec@gmail.com',
    'password': 'wdobshjdcpeyzwxv',
}

def smtp_sendEmail(config, msg):
    context = ssl.create_default_context()
    smtp = smtplib.SMTP_SSL(config['host'],
                            port=config['port'],
                            context=context)
    smtp.login(config['username'], config['password'])
    smtp.send_message(msg)
    smtp.close()
