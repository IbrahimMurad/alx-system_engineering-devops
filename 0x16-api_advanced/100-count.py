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
        [print(title) for title in title_arr]
        next_page = recurse(subreddit, hot_list)
        title_arr.extend(next_page)
        return title_arr
    else:
        if hot_list:
            return []
        else:
            return None


def count_words(subreddit, word_list):
    all_titles = " ".join(recurse(subreddit))
    titles_words = [word for word in all_titles.split(' ') if word]
    word_list = [word for word in " ".split(word_list) if word]
    [print("{}: {}".format(
        word, titles_words.count(word)
    )) for word in word_list]
