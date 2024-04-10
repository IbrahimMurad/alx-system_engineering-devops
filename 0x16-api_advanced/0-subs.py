#!/usr/bin/python3
"""This module defines a functions that
fetches the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data')
            return data.get('subscribers')
        else:
            return 0
    except Exception:
        return 0
