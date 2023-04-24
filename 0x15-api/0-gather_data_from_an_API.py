#!/usr/bin/python3
"""gather data from an api"""


import sys
import requests


if __name__ == "__main__":
    arg1 = sys.argv[1]
    url1 = "https://jsonplaceholder.typicode.com/users/"+ arg1
    url2 = "https://jsonplaceholder.typicode.com/users/"+ arg1 + "/todos"
    req = requests.get(url1)
    name = req.json().get('name')
    req2 = requests.get(url2)
    tasks = req2.json()
    titles = []
    for records in tasks:
        if (records.get("completed")) is True:
            titles.append(records.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(name, len(titles), len(tasks)))
    for t in titles:
        print("\t{}".format(t))
