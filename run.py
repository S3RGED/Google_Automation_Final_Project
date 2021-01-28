#!/usr/bin/env python3
import os
import requests
import re

path = 'supplier-data/descriptions/'
file_list = os.listdir(path)
file_list.sort()
pattern = r" \w+"
def read_file(file):
  with open (path + file) as f:
    description_list = []
    description_dict = {}
    description_list = f.read().splitlines()
    description_dict['name'] = description_list[0]
    description_dict['weight'] = re.sub(pattern, '', description_list[0] )
    description_dict['description'] = description_list[2] 
    description_dict['image'] = file.split(".")[0] + ".jpeg"
  return description_dict


for file in file_list:
  p = read_file(file)
  print(p) 


"""
def main():
  for file in file_list:
    p = read_file(file)
    response = requests.post("http://35.193.74.73/feedback", json=p) 
    print(response.status_code)


if __name__ == "__main__":
    main()
"""
