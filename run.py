#!/usr/bin/env python3
import os
import requests
import re


path = 'supplier-data/descriptions/'
file_list = os.listdir(path)
file_list.sort()

def read_file(file):

    pattern = r"(\d+)( \w+)"
    description_list = []
    description_dict = {}

    with open (path + file) as f:
        description_list = f.read().splitlines()
        no_lbs = re.search(pattern, description_list[1])
        description_dict['name'] = description_list[0]
        description_dict['weight'] = no_lbs.group(1)
        description_dict['description'] = description_list[2]
        description_dict['image'] = file.split(".")[0] + ".jpeg"

    return description_dict


def upload():
    for file in file_list:
        p = read_file(file)
        response = requests.post("http://35.193.74.73/feedback", json=p)
        print(response.status_code)



if __name__ == "__main__":
    upload()
    
