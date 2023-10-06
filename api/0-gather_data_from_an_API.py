import requests

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
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
    print(f"Employee {employee_name[:18]:<18} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Print titles of completed tasks
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    try:
        # Accept an integer as a parameter (employee ID)
        employee_id = int(input("Enter an employee ID: "))
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid input. Please enter an integer employee ID.")
