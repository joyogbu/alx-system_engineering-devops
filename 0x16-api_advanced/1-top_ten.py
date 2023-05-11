#!/usr/bin/python3
"""print top ten """


import requests


def top_ten(subreddit):
    """defining the function"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        print ("None")
        return
    results = req.json()
    myData = results.get("data").get("children")
    for i in range(2):
        print(myData[i].get("data").get("title"))
