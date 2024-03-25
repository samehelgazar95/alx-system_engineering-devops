#!/usr/bin/python3
""" Fetching data """
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    filename = 'todo_all_employees.json'
    url = 'https://jsonplaceholder.typicode.com'

    users = get(f"{url}/users").json()
    all_todos = get(f"{url}/todos").json()

    json_data = {}
    names = {}
    for user in users:
        id = user.get('id')
        json_data[id] = []
        names[id] = user.get('username')

    for t in all_todos:
        id = t.get('userId')
        temp = {}
        temp['username'] = names.get(id)
        temp['task'] = t.get('title')
        temp['completed'] = t.get('completed')
        json_data[id].append(temp)

    with open(filename, 'w') as file:
        json.dump(json_data, file)
