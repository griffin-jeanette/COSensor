from twilio.rest import Client
from keys import passwords
import gmail as mail
import os, os.path
from google_auth_oauthlib.flow import InstalledAppFlow

def sendText(contactInfo):
    account_sid = passwords["twilio"]["account_sid"]
    auth_token = passwords["twilio"]["auth_token"]
    client = Client(account_sid, auth_token)

    for person in contactInfo:

        phoneNum = '+' + person["phoneNum"].replace('-', '')

        message = client.messages \
                        .create(
                             body="WARNING: Dangerous levels of Carbon Monoxide have been detected",
                             from_='+12058130652',
                             to=phoneNum)

def sendEmail(contactInfo):

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/gmail.send"]

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds/serviceAccount.json"

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'creds/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # email each person in the contact list
    for person in contactInfo:
        email = person["emailAddress"]

        to = "griffinjeanette25@gmail.com"
        sender = "basnetnpritam@gmail.com"
        text = "WARNING: Dangerous levels of Carbon Monoxide have been detected"
        subject = "CO Level Warning"

        message1= mail.create_message(sender, to, text, subject)

        mail.send_message(service, sender, message1)



def sendAlert(contactInfo):
    sendText(contactInfo)
    sendEmail(contactInfo)
