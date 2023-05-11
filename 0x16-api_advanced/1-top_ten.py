#!/usr/bin/python3
"""print top ten """


import requests


def top_ten(subreddit):
    """defining the function"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    req = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)
    if req.status_code == 404:
        print("None")
        return
    results = req.json()
    myData = results.get("data").get("children")
    for i in range(10):
        print(myData[i].get("data").get("title"))
