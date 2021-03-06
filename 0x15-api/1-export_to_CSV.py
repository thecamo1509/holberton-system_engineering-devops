#!/usr/bin/python3
""" Script to read an API for a given employee ID """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]})
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={"id": argv[1]})
    user_name = user.json()[0]
    user_id = user.json()[0]["id"]
    with open('{}.csv'.format(user_id), mode='w') as csv_file:
        csv_file_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks.json():
            task_status = task.get('completed')
            task_title = task.get('title')
            csv_file_writer.writerow([user_id, user_name.get('username'),
                                     task_status,
                                     task_title])
