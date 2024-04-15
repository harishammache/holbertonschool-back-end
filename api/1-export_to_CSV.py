#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


import requests
from sys import argv
import csv


def employee_id(employe_id):
    """returns information about his/her TODO list progress."""

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employe_id}"
    url_name = f"https://jsonplaceholder.typicode.com/users/{employe_id}"
    response_name = requests.get(url_name)
    employee_data = response_name.json()
    EMPLOYEE_NAME = employee_data['name']

    response_todo = requests.get(url)
    todos = response_todo.json()
    todo_list = []

    NUMBER_OF_DONE_TASKS = 0
    for completed in todos:
        if completed['completed']:
            NUMBER_OF_DONE_TASKS += 1
            todo_list.append([employe_id, EMPLOYEE_NAME,
                             "Completed", completed['title']])
        else:
            todo_list.append([employe_id, EMPLOYEE_NAME,
                             "Not Completed", completed['title']])
    TOTAL_NUMBER_OF_TASKS = len(todos)

    csv_file_name = f"{employe_id}.csv"
    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        writer.writerows(todo_list)


if __name__ == "__main__":
    employee_id(int(argv[1]))
