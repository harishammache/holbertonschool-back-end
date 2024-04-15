#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


from sys import argv
import requests


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
    print(f"Employee {employee_name} is done with tasks\
({num_completed_tasks}/{total_tasks}):")
    for completed in todos:
        if completed['completed']:
            num_completed_tasks += 1
            print(f"\t {completed['title']}")
    total_tasks = len(todos)


if __name__ == "__main__":
    employee_id(int(argv[1]))
