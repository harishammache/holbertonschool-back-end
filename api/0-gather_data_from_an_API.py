#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


import requests
from sys import argv


def employee_id(employe_id):
    """returns information about his/her TODO list progress."""

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employe_id}"
    url_name = f"https://jsonplaceholder.typicode.com/users/{employe_id}"
    response_name = requests.get(url_name)
    employee_data = response_name.json()
    EMPLOYEE_NAME = employee_data['name']

    response_todo = requests.get(url)
    todos = response_todo.json()

    NUMBER_OF_DONE_TASKS = 0
    for completed in todos:
        if completed['completed']:
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(todos)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for TASK_TITLE in todos:
        if TASK_TITLE['completed']:
            print(f"\t {TASK_TITLE['title']}")


if __name__ == "__main__":
    employee_id(int(argv[1]))
