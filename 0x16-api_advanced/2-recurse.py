#!/usr/bin/python3
"""print recursively """


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """defining the function"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after
        "count": count
        "limit": 10
    }
    req = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)
    if req.status_code == 404:
        return None
    results = req.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
