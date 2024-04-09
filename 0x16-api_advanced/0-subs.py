#!/usr/bin/python3
"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    Fetching subreddit
        Return: the number of subscribers (not active users, total subscribers)
        for a given subreddit, if an invalid subreddit is given, return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        res = get(url, headers={'User-agent': 'app/1.0'})
        data = res.json()
        return data['data']['subscribers']
    except Exception as e:
        return (0)
