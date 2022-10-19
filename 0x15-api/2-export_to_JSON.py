#!/usr/bin/python3
"""Script that returns info using REST API."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(userId), verify=False).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    task_list = []
    for todo in user_todos:
        task_dict = {}
        task_dict["task"] = todo["title"]
        task_dict["completed"] = todo["completed"]
        task_dict["username"] = user["username"]
        task_list.append(task_dict)
    json_obj = {userId: task_list}
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
