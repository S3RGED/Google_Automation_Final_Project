#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib





def generate_email(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()
    sender = "automation@example.com"
    recipient = "<enter username>"
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = "Upload Completed - Online Fruit Store"
    body = """All fruits are uploaded to our website successfully. A detailed list is attached to this email."""
    message.set_content(body)
    attachment_path = "/tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open (attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype = mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment_path))

    return message

print(generate_email())

def send_email():
