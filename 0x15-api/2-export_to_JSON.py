#!/usr/bin/python3
"""gather data from an api"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    url1 = "https://jsonplaceholder.typicode.com/users/" + arg1
    url2 = "https://jsonplaceholder.typicode.com/users/" + arg1 + "/todos"
    req = requests.get(url1)
    name = req.json().get('username')
    req2 = requests.get(url2)
    tasks = req2.json()
    filename = "{}.json".format(arg1)
    with open(filename, "w") as jsonfile:
        json.dump({arg1: [{"task": task.get('title'), "completed": task.get('completed'), "username": name} for task in tasks]}, jsonfile)
