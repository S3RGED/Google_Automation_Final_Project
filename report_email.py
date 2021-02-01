#!/usr/bin/env python3

import os
import datetime
import reports
import run
import emails



path = 'supplier-data/descriptions/'
file_list = os.listdir(path)
file_list.sort()

name_weight = ""


for file in file_list:
    file_data = run.read_file(file)
    name = file_data.get("name")
    weight = file_data.get("weight")
    name_weight += f"name: {name}<br />weight: {weight} lbs<br /><br />"

if __name__ == "__main__":
    attachment = "/tmp/processed.pdf"
    title = f"Processed Update on {datetime.date.today().strftime('%b %d, %Y')}"
    paragraph = name_weight
    reports.generate_report(attachment, title, paragraph)


    sender = "automation@example.com"
    recipient = "<enter username>"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    

    emails.send_email(emails.generate_email(sender, recipient, subject, body, attachment_path))
