#!/usr/bin/python3
"""Gather data from an API and export it to a JSON file."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <USER_ID>")
        exit()

    user_id = argv[1]

    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    user_name = user_info.get('username')

    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                             .format(user_id)).json()

    user_tasks = [{"task": task.get('title'), "completed": task.get('completed'), "username": user_name}
                  for task in todo_list]

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump({user_id: user_tasks}, json_file)

    print("JSON file generated successfully!")
