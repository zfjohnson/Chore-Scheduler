import os
import smtplib
from email.message import EmailMessage
import ssl
from Person import Person

port = 465
email_server = 'smtp.gmail.com'

sender_email = os.environ.get("EMAIL")
password_email = os.environ.get("PASSWORD")
receiver_email = 'quexilion@gmail.com'

subject = 'Weekly Duties'
body = """
    Good morning Americans, get ready to do some work. Here is this week's delectably delegated duties:

"""

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email
msg["BCC"] = sender_email
msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(email_server, port, context=context) as smtp:
    smtp.login(sender_email, password_email)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
