tasks = {}
task_id = 1

def add(tasks):
    global task_id
    a = input("Enter Task: ")
    tasks[task_id] = {"task": a, "status": "No"}
    task_id += 1

def display(tasks):
    if not tasks:
        print("Tasks are Empty..")
        return
    else:
        print(f"{'No':<5} {'Task':<30} {'Completed (Yes/No)'}")
        print("-" * 50)
        for tid, ta in tasks.items():
            print(f"{tid:<5} {ta['task']:<30} {ta['status']}")

def update(tasks):
    display(tasks)
    while True:
        try:
            choice = int(input("Enter task number to update (0 to exit): "))
            if choice == 0:
                break
            if choice in tasks:
                c = input("Mark as completed? (y/n): ").strip().lower()
                if c == 'y':
                    tasks[choice]['status'] = "Yes"
                    print("Task marked as completed!")
                else:
                    tasks[choice]['status'] = "No"
                    print("Task marked as not completed.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            continue
                        
def delete(tasks):
    display(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if choice in tasks:
            tasks.pop(choice)
            print("Task deleted successfully.")
        else:
            print("Invalid task number...")
    except ValueError:
        print("Please enter a number..")    

print("Welcome To To-Do.....")
while True:
    print("""
    1. Press 1 to add a task.
    2. Press 2 to update a task.
    3. Press 3 to delete a task.
    4. Press 4 to display tasks.
    5. Press 5 to Exit.
    """)
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        add(tasks)
    elif choice == '2':
        update(tasks)
    elif choice == '3':
        delete(tasks)
    elif choice == '4':
        display(tasks)
    elif choice == '5':
        print("Bye... Have a Good day!\n")
        exit()
    else:
        print("Invalid input..")
