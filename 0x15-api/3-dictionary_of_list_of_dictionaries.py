#!/usr/bin/python3
"""gather data from an api"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url1).json()
    with open("todo_all_employees.json", "w") as jsonfile:
        for users in req:
            json.dump({users.get('id'): [{
                "username": users.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
                } for task in requests.
                get("https://jsonplaceholder.typicode.com/users/{}/todos".
                    format(users.get('id'))).json()]}, jsonfile)
