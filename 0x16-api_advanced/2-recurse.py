#!/usr/bin/python3
"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], page=1, limit=100):
    """
    Fetching subreddit
        Return: the number of subscribers (not active users, total subscribers)
        for a given subreddit, if an invalid subreddit is given, return 0.
    result = {
    'data': {
        'children': {
            'data':{
                'title': '.......'
                }
            },
        'children': {
            'data':{
                'title': '.......'
                }
            },
        'after': '...'
        }
    }
    """
    if len(hot_list) >= limit:
        return hot_list

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'ALX'}
    params = {"page": page}

    response = get(url, headers=headers, params=params,
                   allow_redirects=False)

    if (response.status_code == 404):
        return None

    result = response.json()

    if 'children' in result['data']:
        for child in result['data']['children']:
            hot_list.append(child['data']['title'])

    if 'after' in result['data']:
        page += 1
        recurse(subreddit, hot_list, page)

    return hot_list
