from mailjet_rest import Client
import os

api_key=os.environ['']
api_secret=os.environ['']
mailjet=Client(api_key, api_secret)

def sendQ(msg):
    data={
        "FromEmail": msg['email'],
        "FromName": "{0} {1}".format(msg['firstname'], msg['lastname']),
        "Subject": "Mesage from {0} {1}".format(msg['firstname'],
                                                msg['lastname']),
        'Text-part': msg["msg"],
        "Recipients":[{"Email":"abelsonmec@gmail.com"}]
    }
    result = mailjet.send.create(data=data)

def sendAp(ap, r):
    data={
        "FromEmail": ap["email"],
        "FromeName": "{0} {1}".format(ap["firstname"], ap["lastname"]),
        "Subject": 'Apliction for {0} {1}'.format(ap["firstname"], ap["lastname"]),
        "Text-part": ap["msg"],
        "Recipients":[{"Email": "abelsonmec@gmail.com"}],
        "Attchments":[{
            "Content-type":"pdf",
            "Filename": "aplication",
            "content": r}]
    }
    result = mailjet.send.create(data=data)
