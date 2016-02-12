from mailjet import Client
import os

api_key=os.environ['']
api_secret=os.environ['']
mailjet=Client(api_key, api_secret)

def sendQ(fn, ln, e, p, c, i, m):
    data={
        "FromEmail": e,
        "FromName": fn + " " + ln,
        "Subject": "Mesage from " + fn + " " + ln,
        'Text-part': m,
        "Recipients":[{"Email":"abelsonmec@gmail.com"}]
    }
    result = mailjet.send.create(data=data)

def sendAp(fn, ln, e, p, po, r, m):
    data={
        "FromEmail": e,
        "FromeName": fn + " " + ln,
        "Subject": 'Apliction for ' + fn + " " + ln,
        "Text-part": m,
        "Recipients":[{"Email": "abelsonmec@gmail.com"}],
        "Attchments":[{"Filename": r}]
    } 
    result = mailjet.sen.create(data=data)
