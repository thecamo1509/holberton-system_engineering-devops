#!/usr/bin/python3
"""Module to display list of hot list"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Recursive function to get the hot list of a subreddit"""
    response = requests.get('https://www.reddit.com/r/{}}/hot.json?after={}'
                            .format(subreddit, after),
                            headers={'User-Agent': 'Camilo@holberton.com'},
                            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        data = response.get('data')
        children = data.get('children')
        for post in children:
            post_data = post.get('data')
            title = post_data.get('title')
            hot_list.append(title)
        after = data.get('after')

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return (None)
