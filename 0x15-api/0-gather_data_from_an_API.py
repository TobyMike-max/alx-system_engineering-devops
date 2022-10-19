#!/usr/bin/python3
"""Script that returns info using REST API."""
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(userId), verify=False).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    completed_tasks = []
    for todo in user_todos:
        if todo['completed'] is True:
            completed_tasks.append(todo['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], len(completed_tasks), len(user_todos)))
    print("\n".join("\t {}".format(todo) for todo in completed_tasks))
