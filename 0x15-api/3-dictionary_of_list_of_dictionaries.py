#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import json
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    all_dict = {}
    for user in users.json():
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": user["id"]})
        task_list = []
        task_dict = {"username": "", "task": "", "completed": ""}
        for task in tasks.json():
            task_dict["username"] = user["username"]
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_list.append(task_dict)
            task_dict = {"username": "", "task": "", "completed": ""}
        all_dict["{}".format(user["id"])] = task_list
    with open("todo_all_employees.json", 'w') as file:
        task_json = json.dump(all_dict, file)
