#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import requests
from sys import argv

tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                     params={"userId": argv[1]})
user = requests.get('https://jsonplaceholder.typicode.com/users',
                    params={"id": argv[1]})

completed = 0
titles = ""
for task in tasks.json():
    if task["completed"] is True:
        completed += 1
        titles += "\t" + " " + task["title"] + "\n"
print("Employee {} is done with tasks({}/{}):".format(user.json()[0]["name"],
      completed, len(tasks.json())))
print(titles, end="")
