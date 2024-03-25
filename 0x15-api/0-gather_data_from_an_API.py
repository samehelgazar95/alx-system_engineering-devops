#!/usr/bin/python3
""" Fetching data """
import requests
from sys import argv


if __name__ == "__main__":
    users_params = {'id': argv[1]}
    todos_params = {'userId': argv[1]}
    done_params = {'userId': argv[1], "completed": "true"}

    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         params=users_params).json()
    done_todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                              params=done_params).json()
    all_todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=todos_params).json()

    name = users[0]["name"]
    done_len = len(done_todos)
    all_todos_len = len(all_todos)

    print('Employee {} is done with tasks({}/{}):'.format(
        name, done_len, all_todos_len))

    for todo in done_todos:
        print("\t{}".format(todo["title"]))
