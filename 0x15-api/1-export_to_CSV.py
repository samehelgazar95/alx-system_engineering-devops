#!/usr/bin/python3
""" Fetching data """
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    filename = f'{user_id}.csv'
    params = {'userId': argv[1]}
    url = 'https://jsonplaceholder.typicode.com'

    user = get(f"{url}/users/{user_id}").json()
    todos = get(f"{url}/todos", params=params).json()

    csv_data = [
        [
            todo.get('userId'),
            user.get('username'),
            todo.get('completed'),
            todo.get('title')
            ] for todo in todos
    ]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
