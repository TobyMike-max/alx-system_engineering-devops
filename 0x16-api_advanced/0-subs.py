#!/usr/bin/python3
"""API query task"""


def number_of_subscribers(subreddit):
    """Function that queries Reddit API and returns the number
    of subscribers in a given subreddit.
    """
    import requests
    url = 'https://www.reddit.com/r/{}/about'.format(subreddit)
    headers = {'User-Agent': 'AppName-api_advanced by RedditUsername-TobyMike'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        result = res.json()['data']
        return result['subscribers']
    else:
        return 0
