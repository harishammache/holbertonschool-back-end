#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


import csv
import requests
from sys import argv


def employee_id(USER_ID):
    """returns information about his/her TODO list progress."""

    url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
    url_name = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_name = requests.get(url_name)
    employee_data = response_name.json()
    USERNAME = employee_data['username']

    response_todo = requests.get(url)
    todos = response_todo.json()

    csv_file_name = f"{USER_ID}.csv"
    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            TASK_COMPLETED_STATUS = task
            TASK_TITLE = task
            writer.writerow([USER_ID, USERNAME,
                             TASK_COMPLETED_STATUS['completed'],
                             TASK_TITLE['title']])


if __name__ == "__main__":
    employee_id(int(argv[1]))
