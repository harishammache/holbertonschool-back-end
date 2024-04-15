#!/usr/bin/python3
from sys import argv
import requests


"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


def employee_id(employe_id):
    """returns information about his/her TODO list progress."""

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employe_id}"
    url_name = f"https://jsonplaceholder.typicode.com/users/{employe_id}"
    response_name = requests.get(url_name)
    employee_data = response_name.json()
    employee_name = employee_data['name']

    response_todo = requests.get(url)
    todos = response_todo.json()

    num_completed_tasks = 0
    total_tasks = 0
    for completed in todos:
        if completed['completed']:
            num_completed_tasks += 1
    total_tasks = len(todos)

    print(f"Employee {employee_name} is done with tasks\
({num_completed_tasks}/{total_tasks}):")
    for completed in todos:
        if completed['completed']:
            print(f"\t {completed['title']}")


if __name__ == "__main__":
    employee_id(int(argv[1]))
