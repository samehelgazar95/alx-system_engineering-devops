#!/usr/bin/python3
""" Fetching data """
from requests import get
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    params = {'userId': argv[1]}

    user = get(f"{url}/users/{user_id}").json()
    all_todos = get(f"{url}/todos", params=params).json()

    completed = [t['title'] for t in all_todos if t['completed']]

    name = user.get('name')
    todos_len = len(all_todos)
    completed_len = len(completed)

    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed_len, todos_len))
    for todo in completed:
        print("\t {}".format(todo))
