#!/usr/bin/python3
"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """_summary_

    Args:
        subreddit (_type_): _description_
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = get(url, headers={'User-Agent': 'app/1.0'})
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
