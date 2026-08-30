# To-Do List Application

A simple **console-based To-Do List application** built with Python for the Python Developer Internship — Task 2.

## Features

- Add new tasks
- View all tasks with numbered output
- Remove tasks by task number
- Save tasks to a text file (`tasks.txt`)
- Automatically load saved tasks when the program starts
- Handles an empty task list
- Handles invalid menu choices and task numbers
- Handles a missing `tasks.txt` file automatically

## Technologies Used

- Python 3
- Command Line / Terminal
- Text-file storage

## Project Structure

```text
To-Do List Application/
│
├── todo.py
├── tasks.txt          # Created automatically when tasks are saved
├── README.md
└── .gitignore
```

## Requirements

- Python 3.x installed on your computer
- VS Code, Command Prompt, PowerShell, or another terminal

No external Python packages are required.

## How to Run

1. Clone or download this repository.
2. Open the repository folder in VS Code or a terminal.
3. Run:

```bash
python todo.py
```

If your system uses `python3`, run:

```bash
python3 todo.py
```

## How to Use

When the program starts, you will see a menu:

```text
====================================
       TO-DO LIST APPLICATION
====================================

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4):
```

### 1. Add Task

Choose `1`, then enter the task you want to save.

```text
Enter your choice (1-4): 1
Enter a task: Complete internship Task 2
Task added successfully.
```

### 2. View Tasks

Choose `2` to display all saved tasks with their numbers.

```text
Your Tasks:
1. Complete internship Task 2
2. Practice Python
```

### 3. Remove Task

Choose `3`, then enter the number of the task you want to remove.

```text
Enter the task number to remove: 1
Removed: "Complete internship Task 2"
```

### 4. Exit

Choose `4` to exit the application. Tasks are saved in `tasks.txt` and will be available the next time the program starts.

## Data Persistence

Tasks are stored one per line in `tasks.txt` using Python's built-in `open()` function. The application reads the file when it starts and writes the updated task list whenever a task is added or removed.

## Concepts Demonstrated

- Python lists
- Functions
- `input()`
- `append()` and `pop()`
- Loops and conditionals
- String handling with `.strip()`
- File handling with `open()`
- Read (`r`) and write (`w`) modes
- `with` context managers
- `try/except` error handling
- Persistent command-line applications

## Internship Task

**Task 2 — Create a To-Do List Application (Console-based)**

The application is designed to meet the task requirements for a Python console application: storing tasks in a list, providing add/view/remove functionality, and saving tasks to a text file for persistence.
