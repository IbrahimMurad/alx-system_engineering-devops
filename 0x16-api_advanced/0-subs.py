#!/usr/bin/python3
""" This module defines a functions that
fetches the number of subscribers for a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """ returns the number of subscribers for subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'MyRedditApp/1.0 (by /u/Aggravating_Page8361)'}
    with requests.get(url, headers=header) as response:
        if response.status_code == 200:
            data = response.json()['data']
            return data['subscribers']
        return 0