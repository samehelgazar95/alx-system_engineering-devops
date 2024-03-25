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
    all_todos = get(f"{url}/todos", params=params).json()

    csv_data = []

    for t in all_todos:
        temp = [t.get('userId'), user.get('username'),
                t.get('completed'), t.get('title')]
        csv_data.append(temp)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
