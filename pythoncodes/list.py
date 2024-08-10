from textual.app import App
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Footer, Button, Label, Input, Static
from rich.text import Text

class TodoItem(Static):
    def __init__(self, task, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.completed = False
        self.button = Button("Complete", id="complete-button")
        self.label = Label(task)
        self.compose()

    def compose(self):
        self.update(Container(self.label, self.button, id="todo-container"))

    def complete_task(self):
        self.completed = True
        self.label.update(Text(self.task, style="strike"))
        self.button.update("Completed")

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "complete-button" and not self.completed:
            self.complete_task()

class TodoApp(App):
    CSS_PATH = "todo.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.tasks = []
        self.input = Input(placeholder="Add a new task", id="task-input")
        self.add_button = Button("Add Task", id="add-task-button")
        self.task_list = VerticalScroll(id="task-list")
        self.clear_button = Button("Clear Completed Tasks", id="clear-button")
        yield Container(self.input, self.add_button, self.clear_button, id="input-container")
        yield self.task_list

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "add-task-button":
            self.add_task(self.input.value)
        elif button.id == "clear-button":
            self.clear_completed_tasks()

    def add_task(self, task):
        if task.strip():
            todo_item = TodoItem(task)
            self.tasks.append(todo_item)
            self.task_list.mount(todo_item)
            self.input.update("")

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.mount(task)

if __name__ == "__main__":
    TodoApp().run()