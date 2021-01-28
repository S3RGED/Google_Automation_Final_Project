#!/usr/bin/env python3
import requests
import re
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = 'supplier-data/images/'
pattern = r".*\.jpeg"

for file in os.listdir(path):
  if re.search(pattern, file) !=None:
    with open(path + file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})




