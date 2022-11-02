#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""
    import requests

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": 'AppName-api_advanced by RedditUsrname-TobyMike-max'
    }
    params = {
            "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        result = res.json()['data']
        [print(c['data']['title']) for c in results['children']]
    else:
        return (print("None"))
