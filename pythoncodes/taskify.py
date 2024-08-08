from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()

class Task:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_tasks(self):
        if not self.tasks:
            console.print(Panel(Text("No tasks found", justify="center"), style="red"))
            return
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", min_width=20)
        table.add_column("Due Date", min_width=12)
        table.add_column("Status", min_width=12)
        table.add_column("Created At", style="dim", min_width=20)
        for i, task in enumerate(self.tasks):
            status = "✅" if task.completed else "❌"
            due_date = task.due_date if task.due_date else "N/A"
            table.add_row(str(i + 1), task.title, due_date, status, task.created_at.strftime("%Y-%m-%d %H:%M"))
        console.print(table)

    def show_menu(self):
        options = {
            "1": "Add Task",
            "2": "Remove Task",
            "3": "Complete Task",
            "4": "List Tasks",
            "5": "Exit"
        }
        console.print(Panel("Task Manager", style="bold blue", title="Menu", title_align="left"))
        for key, value in options.items():
            console.print(f"[bold magenta]{key}[/bold magenta]: {value}")
        return Prompt.ask("Choose an option", choices=list(options.keys()), default="5")

def main():
    manager = TaskManager()
    while True:
        choice = manager.show_menu()
        if choice == "1":
            title = Prompt.ask("Enter task title")
            due_date = Prompt.ask("Enter due date (YYYY-MM-DD) or leave blank", default="")
            manager.add_task(title, due_date if due_date else None)
        elif choice == "2":
            index = int(Prompt.ask("Enter task ID to remove")) - 1
            manager.remove_task(index)
        elif choice == "3":
            index = int(Prompt.ask("Enter task ID to mark as complete")) - 1
            manager.complete_task(index)
        elif choice == "4":
            manager.list_tasks()
        elif choice == "5":
            console.print(Panel("Goodbye!", style="bold green"))
            break

if __name__ == "__main__":
    main()
