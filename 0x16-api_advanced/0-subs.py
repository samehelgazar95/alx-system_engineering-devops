#!/usr/bin/python3
from requests import get
import json
"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""


def number_of_subscribers(subreddit):
    """
    Fetching subreddit
        Return: the number of subscribers (not active users, total subscribers)
        for a given subreddit, if an invalid subreddit is given, return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        res = get(url, headers={'User-agent': 'elgazar'}, allow_redirects=False)
        data = res.json()
        return data['data']['subscribers']
    except Exception as e:
        return (0)
