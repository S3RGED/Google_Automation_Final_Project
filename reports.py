#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    today_date = date.today()
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    empty_line = Spacer(1, 20)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, empty_line, report_info, empty_line])
