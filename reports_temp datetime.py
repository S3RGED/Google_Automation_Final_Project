#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date


def generate_report(attachment, title, paragraph):
    today_date = date.today()
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    empty_line = Spacer(1, 20)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, empty_line, report_info, empty_line])


attachment = "/tmp/processed.pdf"
title = f"Processed Update on {date.today().strftime('%b %d, %Y')}"
paragraph = f"name: Apple <br /> weight: 500 lbs"
generate_report(attachment, title, paragraph)
