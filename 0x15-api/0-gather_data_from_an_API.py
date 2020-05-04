#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import requests
from sys import argv

if __name__ == "__main__":
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
    user_name = user.json()[0]["name"]
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          completed, len(tasks.json())))
    print(titles, end="")
