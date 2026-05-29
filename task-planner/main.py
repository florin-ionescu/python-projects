import tasks


def task_menu():
    print("Welcome to the task planner")
    print("\n1. Add a new task")
    print("2. Search task by keywords." )
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Mark as completed")
    print("6. Save and exit")
    choice = print(input("\nPlease choose an option from the menu: "))

def main(tasks):
    task_menu()
    while True:
        choice = int(input("\nPlease choose an option from the menu: "))
        if choice == 1:
            add_task()

if __name__ == "__main__":
    main()