#!/usr/bin/python3
"""This module defines a functions that
fetches the number of subscribers for a subreddit.
"""

import requests


def top_ten(subreddit):
    """ returns the number of subscribers for subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    para = {'limit': 10}
    try:
        response = requests.get(
            url,
            headers=header,
            params=para,
            allow_redirects=False
            )
        if response.status_code == 200:
            data = response.json()['data']['children']
            for post in data:
                print(post.get('data').get('title'))
        else:
            print('None')
    except Exception:
        print('None')
