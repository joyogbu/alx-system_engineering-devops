#!/usr/bin/python3
"""print top ten """


import requests


def top_ten(subreddit):
    """defining the function"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
  #{}/popular/".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    '''params = {
        "limit": 3
    }'''
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    results = req.json()
    myData = results.get("data").get("children")
    for i in range(10):
        print(myData[i].get("data").get("title"))
