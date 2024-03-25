#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information
about his/her TODO list progress and export data in the CSV format.
"""

from json import loads
from sys import argv
from urllib.request import urlopen


if __name__ == '__main__':
    employee_ID = int(argv[1])

    todos_data_fetched = urlopen('https://jsonplaceholder.typicode.com/todos')
    all_todos = loads(todos_data_fetched.read().decode())
    todo_of_employee = [x for x in all_todos if x.get('userId') == employee_ID]

    users_data_fetched = urlopen('https://jsonplaceholder.typicode.com/users')
    users = loads(users_data_fetched.read().decode())
    EMPLOYEE_NAME = next(
        x for x in users if x.get('id') == employee_ID
        ).get('username')

    with open('{}.csv'.format(employee_ID), mode='a', encoding='utf-8') as f:
        for task in todo_of_employee:
            f.write('"{}","{}","{}","{}"\n'.format(
                employee_ID,
                EMPLOYEE_NAME,
                task.get('completed'),
                task.get('title')
                ))
