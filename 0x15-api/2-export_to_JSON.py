#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import json
import requests
from sys import argv

if __name__ == "__main__":
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]})
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={"id": argv[1]})
    task_list = []
    user_id = user.json()[0]["id"]
    main_dict = {"{}".format(user_id): task_list}
    task_dict = {"task": "", "completed": "", "username": ""}
    for task in tasks.json():
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = user.json()[0]["name"]
        task_list.append(task_dict)
        task_dict = {"task": "", "completed": "", "username": ""}
    with open("{}.json".format(user_id), 'w') as file:
        task_json = json.dump(main_dict, file)
