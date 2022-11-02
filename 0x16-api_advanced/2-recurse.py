#!/usr/bin/python3
""" Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced by TobyMike-max"
    }
    params = {
            "after": after,
            "count": count,
            "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        result = res.json()['data']
        after = result['after']
        count += result['dist']
        for c in result['children']:
            hot_list.append(c['data']['title'])
    else:
        return (None)

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
