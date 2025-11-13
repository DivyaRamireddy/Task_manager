# task_manager.py
# A slightly complex mini project: Command-Line Task Manager ✔️

import datetime

tasks = []

def add_task():
    title = input("Enter task title: ")
    due = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Try again.")
        return

    tasks.append({
        "title": title,
        "due": due_date,
        "completed": False
    })
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks found.\n")
        return
    
    print("\n📋 Your Tasks:")
    print("-----------------------------")
    for i, task in enumerate(tasks, 1):
        status = "✔️ Completed" if task["completed"] else "❌ Pending"
        print(f"{i}. {task['title']}  |  Due: {task['due']}  |  {status}")
    print()


def mark_completed():
    view_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to mark as completed: "))
        tasks[index - 1]["completed"] = True
        print("Task marked as completed!\n")
    except:
        print("Invalid choice!\n")


def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to delete: "))
        removed = tasks.pop(index - 1)
        print(f"Deleted task: {removed['title']}\n")
    except:
        print("Invalid choice!\n")


def menu():
    print("""
========= TASK MANAGER =========
1. Add Task
2. View All Tasks
3. Mark Task as Completed
4. Delete a Task
5. Exit
================================
""")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid option! Try again.\n")
