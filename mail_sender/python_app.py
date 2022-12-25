from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import os
import sys
if(len(sys.argv) !=2):
    print('[-] Run the script with python_app.py <email_of_receiver>')
    sys.exit()
load_dotenv()
email_sender = os.getenv('Email')
email_pasword = os.getenv('Password')
email_receiver = sys.argv[1]

subject = "This Is A Test Message"
body="""
Hello This is a test message from Python
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_pasword)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
