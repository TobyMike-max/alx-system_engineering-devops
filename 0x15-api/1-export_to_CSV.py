#!/usr/bin/python3
"""Script that returns info using REST API."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(userId), verify=False).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    with open("{}.csv".format(userId), 'w', newline="") as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in user_todos:
            taskwriter.writerow([int(userId), user['username'],
                                todo['completed'], todo['title']])
