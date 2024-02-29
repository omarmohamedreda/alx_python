"""
This module contains an api that exports to JSON
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['username']  # Changed from 'name' to 'username'

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Create JSON data
    json_data = {
        employee_id: [{"task": todo['title'], "completed": todo['completed'], "username": employee_name} for todo in todos]
    }

    # Create JSON file name
    json_filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

   
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    json_filename = get_employee_todo_progress(employee_id)
    
