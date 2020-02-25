# program to alert users that CO levels are above safety threshold

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from keys import passwords


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

def sendText(contactInfo):
    account_sid = passwords["twilio"]["account_sid"]
    auth_token = passwords["twilio"]["auth_token"]
    client = Client(account_sid, auth_token)


    for person in contactInfo:

        phoneNum = '+' + person["phoneNum"].replace('-', '')

        message = client.messages \
                        .create(
                             body="WARNING: dangerous levels of Carbon Monoxide have been detected",
                             from_='+12058130652',
                             to=phoneNum)

    print(message.sid)


def sendAlert(contactInfo):
    sendText(contactInfo)
    #sendEmail(contactInfo)

#sendAlert()
