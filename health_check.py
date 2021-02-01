#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil
import emails


def check_disk_full():
    """Returns True if there is enough free disk space, False otherwise"""
    du = shutil.disk_usage('/')
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total

    if percent_free < 20:
        return True
    return False

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 80

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("127.0.0.1")
        return False
    except:
        return True

def check_memfree():
    mu = psutil.virtual_memory()
    if mu[1] < 500000000:
        return True
    return False

def main():
    checks=[
    (check_disk_full, "Error - Available disk space is less than 20%"),
    (check_cpu_constrained, "Error - CPU usage is over 80%"),
    (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1"),
    (check_memfree, "Error - Available memory is less than 500MB")
    ]
    everything_ok = True
    for check, subject in checks:
        if check():
            #print(subject)
            sender = "automation@example.com"
            recipient = "<ENTER USERNAME>"
            body = "Please check your system and resolve the issue as soon as possible."
            emails.send_email(emails.generate_error_report(sender, recipient, subject, body))


            everything_ok = False
    if not everything_ok:
        sys.exit(1)

    #print("Everything is OK.")
    sys.exit(0)

main()
