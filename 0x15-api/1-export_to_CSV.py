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
    for task in tasks:
        csvid = task.get('userId')
        filename = "{}" ".csv".format(csvid)
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in tasks:
            writer.writerow([csvid, name, row.get('completed'),
                            row.get('title')])
