#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information
about his/her TODO list progress and export data in the json format.
"""

import json
from sys import argv
from requests import get

todo_url = 'https://jsonplaceholder.typicode.com/todos'
users_url = 'https://jsonplaceholder.typicode.com/users'

if __name__ == '__main__':
    employee_ID = int(argv[1])

    all_todos = get(todo_url).json()
    todo_of_employee = [x for x in all_todos if x.get('userId') == employee_ID]

    users = get(users_url).json()
    username = next(
        x for x in users if x.get('id') == employee_ID
        ).get('username')

    task_list = []
    for todo in todo_of_employee:
        completed = todo.get('completed')
        todo.pop('completed')
        todo.update({
            'task': todo.get('title'),
            'completed': completed,
            'username': username
            })
        todo.pop('title')
        todo.pop('id')
        todo.pop('userId')
        task_list.append(todo)
    dict_to_export = {str(employee_ID): task_list}
    with open(str(employee_ID) + ".json", 'w') as f:
        json.dump(dict_to_export, f)
