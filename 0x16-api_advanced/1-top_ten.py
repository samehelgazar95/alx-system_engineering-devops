#!/usr/bin/python3
"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    """
    Fetching subreddit
        Return: the number of subscribers (not active users, total subscribers)
        for a given subreddit, if an invalid subreddit is given, return 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    res = get(url, headers={'User-Agent': 'app/1.0'})
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
