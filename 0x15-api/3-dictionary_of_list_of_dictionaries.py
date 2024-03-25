#!/usr/bin/python3
""" Fetching data """
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    filename = 'todo_all_employees.json'
    url = 'https://jsonplaceholder.typicode.com'

    users = get(f"{url}/users").json()
    todos = get(f"{url}/todos").json()

    json_data = {
        user.get('id'): [
            {
                'username': user.get('username'),
                'task': todo.get('title'),
                'completed': todo.get('completed')
            } for todo in todos if todo.get('userId') == user.get('id')
            ] for user in users
    }

    with open(filename, 'w') as file:
        json.dump(json_data, file)
