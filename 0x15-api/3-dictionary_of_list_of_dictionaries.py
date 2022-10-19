#!/usr/bin/python3
"""Script that returns info using REST API."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    json_dict = {}
    for i in range(0, 10):
        user_todos = requests.get(
                    'https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(i), verify=False).json()
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(i)).json()
        task_list = []
        for todo in user_todos:
            task_dict = {}
            task_dict["username"] = user["username"]
            task_dict["task"] = todo["title"]
            task_dict["completed"] = todo["completed"]
            task_list.append(task_dict)
        json_dict[i] = task_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
