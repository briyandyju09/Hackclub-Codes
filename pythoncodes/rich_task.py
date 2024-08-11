from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich.text import Text

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def toggle_complete(self):
        self.completed = not self.completed

class TaskListApp:
    def __init__(self):
        self.tasks = []
        self.console = Console()

    def display_tasks(self):
        table = Table(title="Task List", box=box.ROUNDED)
        table.add_column("ID", style="dim", width=6)
        table.add_column("Task Description", style="cyan")
        table.add_column("Status", style="green")

        if not self.tasks:
            self.console.print("No tasks added yet.", style="bold yellow")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✅" if task.completed else "❌"
                table.add_row(str(index), task.description, status)

            self.console.print(table)

    def add_task(self):
        description = Prompt.ask("Enter the task description")
        if description:
            self.tasks.append(Task(description))
            self.console.print(f"Task '{description}' added successfully.", style="bold green")

    def remove_task(self):
        self.display_tasks()
        task_id = Prompt.ask("Enter the task ID to remove")
        if task_id.isdigit():
            index = int(task_id) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                self.console.print(f"Task '{removed_task.description}' removed.", style="bold red")
            else:
                self.console.print("Invalid task ID.", style="bold yellow")
        else:
            self.console.print("Please enter a valid number.", style="bold yellow")

    def toggle_task(self):
        self.display_tasks()
        task_id = Prompt.ask("Enter the task ID to mark as complete/incomplete")
        if task_id.isdigit():
            index = int(task_id) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].toggle_complete()
                self.console.print(f"Task '{self.tasks[index].description}' status toggled.", style="bold blue")
            else:
                self.console.print("Invalid task ID.", style="bold yellow")
        else:
            self.console.print("Please enter a valid number.", style="bold yellow")

    def run(self):
        while True:
            self.console.print("\n[1] Add Task  [2] Remove Task  [3] Toggle Task  [4] View Tasks  [5] Exit", style="bold magenta")
            choice = Prompt.ask("Choose an option")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.toggle_task()
            elif choice == "4":
                self.display_tasks()
            elif choice == "5":
                self.console.print("Exiting the task manager. Goodbye!", style="bold cyan")
                break
            else:
                self.console.print("Invalid choice, please try again.", style="bold yellow")

if __name__ == "__main__":
    app = TaskListApp()
    app.run()
