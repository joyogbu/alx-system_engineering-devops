#!/usr/bin/python3
"""queries an api and return the number of subscribers
for a given reddit"""


import requests
import requests.auth


def number_of_subscribers(subreddit):
    """defining the function """
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return 0
    result = req.json().get("data")
    return(result.get("subscribers"))
