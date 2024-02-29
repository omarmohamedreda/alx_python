import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Calculate TODO list progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Print progress information
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    # Print titles of completed tasks
    count = 0
    for todo in todos:
        count += 1
        if todo['completed']:
            print(f"\t {todo['title']}")
        


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
