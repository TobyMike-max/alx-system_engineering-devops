#!/usr/bin/python3
"""Script that returns info using REST API."""
import requests
from sys import argv


if __name__ == "__main__":
    user_Id = argv[1]
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?user_Id={}'
                        .format(user_Id), verify=False).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_Id)).json()
    completed_tasks = []
    for task in todo:
        if task['completed'] is True:
            completed_tasks.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".
            format(user['name'], len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
