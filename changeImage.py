#!/usr/bin/env python3

import os
from PIL import Image
import re

cwd = os.getcwd()
path = 'supplier-data/images/'
pattern = r".*\.tiff"

for file in os.listdir(path):
  if re.search(pattern, file) !=None:
    im = Image.open(path + file)
    im.convert('RGB').resize((600, 400)).save(path + file.split('.')[0] + '.jpeg', 'JPEG')
    im.close()
