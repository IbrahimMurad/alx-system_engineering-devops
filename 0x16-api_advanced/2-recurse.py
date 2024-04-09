#!/usr/bin/python3
"""This module defines a functions that
fetches the number of subscribers for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """ returns a list containing the titles of all hot
    articles for a given subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    para = {'after': hot_list[-1]} if hot_list else {}
    response = requests.get(
        url,
        headers=header,
        params=para,
        allow_redirects=False
        )
    if response.status_code == 200:
        data = response.json()['data']
        hot_list.append(data['after'])
        title_arr = [post['data']['title'] for post in data['children']]
        next_page = recurse(subreddit, hot_list)
        title_arr.extend(next_page)
        return title_arr
    else:
        if hot_list:
            return []
        else:
            return None
