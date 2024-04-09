#!/usr/bin/python3
from requests import get
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
    url = f'https://www.reddit.com/r/{subreddit}.json?'
    try:
        res = get(url, headers={'User-agent': 'elgazar'}, allow_redirects=False)
        data = res.json()
        return (data['data']['children'][0]['data']['subreddit_subscribers'])
    except Exception as e:
        return (0)
