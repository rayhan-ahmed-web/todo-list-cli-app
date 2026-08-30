"""Console-based persistent To-Do List Application."""

TASK_FILE = "tasks.txt"


def load_tasks(filename=TASK_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename=TASK_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Enter the task number to remove: ").strip())
        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f'Removed: "{removed}"')
    except ValueError:
        print("Please enter a valid task number.")


def main():
    tasks = load_tasks()
    print("=" * 36)
    print("       TO-DO LIST APPLICATION")
    print("=" * 36)
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
