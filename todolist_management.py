import datetime
import random
import time
import os
import calendar

tasks = []

def clear_screen():
    os.sys("cls" if os.name == "nt" else "clear")

def add_task():
    print("\n--- ADD TASK ---")

    task = input("Enter your task: ")

    if task == "":
        print("Task cannot be empty!")
    else:
        task_id = random.randint(1000, 9999)

        tasks.append({
            "id": task_id,
            "task": task,
            "status": "Pending",
            "date": str(datetime.date.today())
        })

        print("Task added successfully!")
        print("Task ID:", task_id)

def view_tasks():
    print("\n--- YOUR TASKS ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i in range(len(tasks)):
        print(
            str(i + 1) + ". " +
            tasks[i]["task"] +
            " [" +
            tasks[i]["status"] +
            "]"
        )
        print("   ID:", tasks[i]["id"])
        print("   Added on:", tasks[i]["date"])

def complete_task():
    print("\n--- COMPLETE TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            print("Task completed successfully!")
        else:
            print("Invalid task number.")

    except:
        print("Please enter a valid number.")

def delete_task():
    print("\n--- DELETE TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number: "))

        if number >= 1 and number <= len(tasks):
            deleted_task = tasks.pop(number - 1)

            print(
                "Task deleted:",
                deleted_task["task"]
            )
        else:
            print("Invalid task number.")

    except:
        print("Please enter a valid number.")

def edit_task():
    print("\n--- EDIT TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number: "))

        if number >= 1 and number <= len(tasks):

            new_task = input(
                "Enter the new task: "
            )

            if new_task == "":
                print("Task cannot be empty.")
            else:
                tasks[number - 1]["task"] = new_task

                print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except:
        print("Please enter a valid number.")
def search_task():
    print("\n--- SEARCH TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    search = input(
        "Enter task name to search: "
    ).lower()

    found = False

    for i in range(len(tasks)):

        if search in tasks[i]["task"].lower():

            print(
                str(i + 1) + ". " +
                tasks[i]["task"] +
                " [" +
                tasks[i]["status"] +
                "]"
            )

            found = True

    if found == False:
        print("Task not found.")

def show_statistics():
    print("\n--- TASK STATISTICS ---")

    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1
        else:
            pending += 1

    print("Total tasks     :", total)
    print("Completed tasks :", completed)
    print("Pending tasks   :", pending)

def show_date():
    print("\n--- CURRENT DATE ---")

    today = datetime.date.today()

    print("Today's date:", today)

def show_time():
    print("\n--- CURRENT TIME ---")

    current_time = time.strftime("%H:%M:%S")

    print("Current time:", current_time)
def set_priority():
    print("\n--- SET PRIORITY ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number: "))

        if number >= 1 and number <= len(tasks):

            print("1. High")
            print("2. Medium")
            print("3. Low")

            choice = input("Choose priority: ")

            if choice == "1":
                priority = "High"
            elif choice == "2":
                priority = "Medium"
            elif choice == "3":
                priority = "Low"
            else:
                print("Invalid priority.")
                return

            tasks[number - 1]["priority"] = priority

            print("Priority set to:", priority)

        else:
            print("Invalid task number.")

    except:
        
        print("Please enter a valid number.")

def show_calendar():
    print("\n--- CALENDAR ---")

    today = datetime.date.today()

    print(calendar.month(
        today.year,
        today.month
    ))
def completion_percentage():
    print("\n--- COMPLETION PERCENTAGE ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    completed = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1

    percentage = (
        completed / len(tasks)
    ) * 100

    print(
        "Completion Percentage:",
        round(percentage, 2),
        "%"
    )

while True:

    print("\n")
    print("================================")
    print("     TO-DO LIST MANAGEMENT")
    print("================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Search Task")
    print("7. Task Statistics")
    print("8. Exit")
    print("9. Show Current Date")
    print("10. Show Current Time")
    print("11. Set Task Priority")
    print("12. Show Calendar")
    print("13. Completion Percentage")
    print("14. Clear Screen")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        edit_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        search_task()

    elif choice == "7":
        show_statistics()

    elif choice == "8":
        print("\nThank you for using To-Do List Management System!")
        break

    elif choice == "9":
        show_date()

    elif choice == "10":
        show_time()

    elif choice == "11":
        set_priority()

    elif choice == "12":
        show_calendar()

    elif choice == "13":
        completion_percentage()

    elif choice == "14":
        clear_screen()

    else:
        print("Invalid choi" \
        "ce. Please try again.")