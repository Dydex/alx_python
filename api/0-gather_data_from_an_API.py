import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetch TODO list for the employee
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate the progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Print the progress information
    print(
        f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Print titles of completed tasks
    for i, task in enumerate(todo_data, start=1):
        if task["completed"]:
            print(f"Task {i} Formatting: OK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid input. Please enter an integer employee ID.")
