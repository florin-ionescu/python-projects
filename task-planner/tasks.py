

def add_task(tasks):
    task_name = input("Describe your task: ")
    task = {
        "task_name": task_name,
        "done": False,
    }
    tasks.append(task)

def search_task(tasks):
    if not tasks:
        print("No tasks found.")

    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not done"
        print(
            f"{index}. {task['task_name']} | "
            f"Status: {status}"
        )

def delete_task():
    pass

def mark_done_task():
    pass

def view_task():
    pass

def save_task():
    pass
