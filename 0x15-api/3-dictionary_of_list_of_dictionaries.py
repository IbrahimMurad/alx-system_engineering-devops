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

    all_todos = get(todo_url).json()
    users = get(users_url).json()

    todo_all_employees = {}
    for user in users:
        username = user.get('username')
        user_id = user.get('id')
        todo_of_employee = [
            x for x in all_todos
            if x.get('userId') == user_id
            ]
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
        todo_all_employees.update({str(user_id): task_list})

    with open("todo_all_employees.json", 'w') as f:
        json.dump(todo_all_employees, f)
