from asyncio import tasks
from tasks import add_task, view_task, delete_task, mark_done_task, search_task, save_task
from storage import load_tasks, save_tasks

def task_menu():
    print("Welcome to the task planner")
    print("\n1. Add a new task")
    print("2. Search task by keywords." )
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Mark as completed")
    print("6. Save and exit")

def main():
    tasks = load_tasks()
    print("Loaded tasks:", tasks)
    print("Number of tasks:", len(tasks))

    while True:
        task_menu()
        choice = input("\nPlease choose an option from the menu: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done_task(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            save_task(tasks)
            print("Task saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


