#!/usr/bin/python3
"""Module to get the subscriber count of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns the number of subs"""
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers={'User-Agent': 'Camilo@holberton'},
                            allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        data = response.get('data')
        subs_count = data.get('subscribers')
        if data and subs_count:
            return subs_count
    return 0
