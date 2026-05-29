

tasks = []

def task_planner():
    # Menu creating - use while loops to go over the code until you tell it to stop
    while True:
        print("\nTask planner\n")
        print("Choose an option: ")
        print("1. Add a task")
        print("2. View all task")
        print("3. Exit")

        # avoids getting the error from typing something incorrect (it must be int)
        try:
            choice = int(input("\nPlease choose an option from the menu: "))
        except ValueError:
            print("Invalid option. Please enter a number: 1, 2 or 3 ")
            continue

        if choice == 1:
            task = input("What is your task, master? ")
            tasks.append(task)
            print("\nTask added\n")
        elif choice == 2:
            if len(tasks) == 0:
                print("\nNo tasks yet.")
            else:
                print("\nYour tasks:")
                for task in tasks:
                    print("-", task)
        elif choice == 3: # this breaks the loop
            print("Loop end")
            break
        else:
            print("Invalid option")

task_planner()