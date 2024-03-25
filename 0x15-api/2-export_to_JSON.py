#!/usr/bin/python3
""" Fetching data """
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    filename = f'{user_id}.json'
    params = {'userId': argv[1]}
    url = 'https://jsonplaceholder.typicode.com'

    user = get(f"{url}/users/{user_id}").json()
    todos = get(f"{url}/todos", params=params).json()

    json_data = {user_id: [
        {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username')
        } for todo in todos
    ]}

    with open(filename, 'w') as file:
        json.dump(json_data, file)
