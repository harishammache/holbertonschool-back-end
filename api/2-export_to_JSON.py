#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


import requests
from sys import argv
import json


def employee_id(USER_ID):
    """returns information about his/her TODO list progress."""

    url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
    url_name = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_name = requests.get(url_name)
    employee_data = response_name.json()
    USERNAME = employee_data['username']

    response_todo = requests.get(url)
    todos = response_todo.json()

    user_tasks = []

    for task in todos:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": USERNAME
        })

    json_file_name = f"{USER_ID}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump({USER_ID: user_tasks}, json_file)


if __name__ == "__main__":
    employee_id(int(argv[1]))
