#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import json
import requests
from sys import argv

if __name__ == "__main__":
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    task_list = []
    user_id = argv[1]
    main_dict = {}
    for task in tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = user.get('username')
        task_list.append(task_dict)
    main_dict[argv[1]] = task_list
    task_json = json.dumps(main_dict)
    with open("{}.json".format(user_id), 'w', newline='') as file:
        file.write(task_json)
