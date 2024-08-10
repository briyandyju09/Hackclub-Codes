from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, Static, Header, Footer
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from datetime import datetime, timedelta

class Task:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.total_time = timedelta()

    def start(self):
        if self.start_time is None:
            self.start_time = datetime.now()

    def stop(self):
        if self.start_time is not None:
            self.total_time += datetime.now() - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.total_time = timedelta()

    def __str__(self):
        time_spent = self.total_time + (datetime.now() - self.start_time if self.start_time else timedelta())
        return f"Task: {self.name}\nTime Spent: {str(time_spent).split('.')[0]}"

class TaskTimerApp(App):
    CSS = """
    Vertical {
        border: round #333;
        padding: 2;
        margin: 1;
        background: #111;
    }
    """

    def __init__(self):
        super().__init__()
        self.tasks = {}
        self.current_task = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Task Timer"),
            Button("Add Task", id="add_task"),
            Button("Start Task", id="start_task"),
            Button("Stop Task", id="stop_task"),
            Button("Reset Task", id="reset_task"),
            Button("View Tasks", id="view_tasks"),
            Button("Exit", id="exit"),
            id="menu"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "add_task":
            self.push_screen(AddTaskScreen(self))
        elif button_id == "start_task":
            self.push_screen(StartTaskScreen(self))
        elif button_id == "stop_task":
            self.push_screen(StopTaskScreen(self))
        elif button_id == "reset_task":
            self.push_screen(ResetTaskScreen(self))
        elif button_id == "view_tasks":
            self.push_screen(ViewTasksScreen(self))
        elif button_id == "exit":
            self.exit()

    def add_task(self, name):
        self.tasks[name] = Task(name)

class AddTaskScreen(Screen):
    def __init__(self, app: TaskTimerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add Task"),
            Input(placeholder="Task Name", id="task_name"),
            Button("Add", id="add"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            task_name = self.query_one("#task_name", Input).value
            self.app.add_task(task_name)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class StartTaskScreen(Screen):
    def __init__(self, app: TaskTimerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Start Task"),
            Input(placeholder="Task Name", id="task_name"),
            Button("Start", id="start"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            task_name = self.query_one("#task_name", Input).value
            task = self.app.tasks.get(task_name)
            if task:
                task.start()
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class StopTaskScreen(Screen):
    def __init__(self, app: TaskTimerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Stop Task"),
            Input(placeholder="Task Name", id="task_name"),
            Button("Stop", id="stop"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "stop":
            task_name = self.query_one("#task_name", Input).value
            task = self.app.tasks.get(task_name)
            if task:
                task.stop()
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class ResetTaskScreen(Screen):
    def __init__(self, app: TaskTimerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Reset Task"),
            Input(placeholder="Task Name", id="task_name"),
            Button("Reset", id="reset"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "reset":
            task_name = self.query_one("#task_name", Input).value
            task = self.app.tasks.get(task_name)
            if task:
                task.reset()
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class ViewTasksScreen(Screen):
    def __init__(self, app: TaskTimerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("View Tasks"),
            Button("Back", id="back"),
            Static(id="tasks_output"),
        )

    def on_screen_opened(self) -> None:
        output = self.query_one("#tasks_output", Static)
        output.update("\n".join(str(task) for task in self.app.tasks.values()))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

if __name__ == "__main__":
    TaskTimerApp().run()