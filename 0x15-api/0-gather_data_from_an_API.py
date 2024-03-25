#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
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
        ).get('name')

    TOTAL_NUMBER_OF_TASKS = len(todo_of_employee)
    DONE_TASKS = [x for x in todo_of_employee if x.get('completed') is True]
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS
        ))
    for task in DONE_TASKS:
        print("\t {}".format(task.get('title')))
