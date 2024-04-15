#!/usr/bin/python3
"""
    using the REST API for a given employee ID
    returns informations about his TODO list progress
"""


import requests
import json


def export_all_tasks():
    """"returns information about his/her TODO list progress."""

    users_url = "https://jsonplaceholder.typicode.com/users"
    response_users = requests.get(users_url)
    users_data = response_users.json()

    all_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        user_tasks_url = f"https://jsonplaceholder\
.typicode.com/todos?userId={user_id}"
        response_tasks = requests.get(user_tasks_url)
        tasks_data = response_tasks.json()

        user_task_list = []

        for task in tasks_data:
            user_task_list.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        all_tasks[user_id] = user_task_list

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks()
