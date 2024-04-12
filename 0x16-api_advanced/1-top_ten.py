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
    listing = 'hot'
    limit = 10
    url = 'https://www.reddit.com/r/{}/{}.json?limit={}'.format(
        subreddit, listing, limit)
    try:
        res = get(url, headers={'User-agent': 'app/1.0'},
                  allow_redirects=False)
        if res.status_code == 200:
            data = res.json()
            for post in data['data']['children']:
                print(post['data']['title'])
    except Exception as e:
        print(None)
