import datetime

tasks = []

class Task:
    def __init__(self, name, priority, due_date, category):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.category = category

def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    name = input("Enter task name: ")
    priority = input("Enter task priority (High, Medium, Low): ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    category = input("Enter task category: ")
    task = Task(name, priority, due_date, category)
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    for index, task in enumerate(tasks):
        print(f"\nTask {index + 1}")
        print("Name:", task.name)
        print("Priority:", task.priority)
        print("Due Date:", task.due_date)
        print("Category:", task.category)

def update_task():
    task_index = int(input("Enter the task number to update: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number!")
        return

    task = tasks[task_index]
    print("\nCurrent Task Details:")
    print("Name:", task.name)
    print("Priority:", task.priority)
    print("Due Date:", task.due_date)
    print("Category:", task.category)

    name = input("Enter updated task name (leave blank to keep current value): ")
    priority = input("Enter updated task priority (leave blank to keep current value): ")
    due_date = input("Enter updated task due date (YYYY-MM-DD) (leave blank to keep current value): ")
    category = input("Enter updated task category (leave blank to keep current value): ")

    if name:
        task.name = name
    if priority:
        task.priority = priority
    if due_date:
        task.due_date = due_date
    if category:
        task.category = category

    print("Task updated successfully!")

def delete_task():
    task_index = int(input("Enter the task number to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number!")
        return

    del tasks[task_index]
    print("Task deleted successfully!")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice! Please try again.")
