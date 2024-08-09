from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class TaskManager(Widget):
    tasks = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.displayed_tasks = []

    def render(self):
        task_list = "\n".join([f"[{'X' if task['completed'] else ' '}] {task['priority']} - {task['description']}" for task in self.displayed_tasks])
        return Vertical(
            Static("Task Prioritization Tool"),
            Static(self.message),
            Static(task_list if task_list else "No tasks available."),
            Button(label="Add Task", id="add"),
            Button(label="Remove Task", id="remove"),
            Button(label="List Tasks by Priority", id="list"),
            Button(label="Complete Task", id="complete"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_task()
        elif button_id == "remove":
            await self.remove_task()
        elif button_id == "list":
            await self.list_tasks_by_priority()
        elif button_id == "complete":
            await self.complete_task()
        await self.refresh()

    async def add_task(self):
        self.message = "Enter task description and priority separated by a comma:"
        await self.refresh()
        desc_priority = await self.ask_user_input()
        if desc_priority:
            description, priority = desc_priority.split(",")
            self.tasks.append({"description": description.strip(), "priority": int(priority.strip()), "completed": False})
            self.message = f"Added task: {description.strip()} with priority {priority.strip()}"

    async def remove_task(self):
        self.message = "Enter task description to remove:"
        await self.refresh()
        description = await self.ask_user_input()
        self.tasks = [task for task in self.tasks if task["description"] != description.strip()]
        self.message = f"Removed task: {description.strip()}"

    async def list_tasks_by_priority(self):
        self.displayed_tasks = sorted(self.tasks, key=lambda task: task["priority"])
        self.message = "Tasks listed by priority:"

    async def complete_task(self):
        self.message = "Enter task description to mark as completed:"
        await self.refresh()
        description = await self.ask_user_input()
        for task in self.tasks:
            if task["description"] == description.strip():
                task["completed"] = True
                self.message = f"Task '{description.strip()}' marked as completed"
                break
        else:
            self.message = f"Task '{description.strip()}' not found"

    async def ask_user_input(self):
        input_widget = Input()
        await self.view.dock(input_widget)
        input_widget.focus()
        await self.wait_for_input(input_widget)
        user_input = input_widget.value
        await input_widget.remove()
        return user_input

    async def wait_for_input(self, input_widget):
        while not input_widget.value:
            await self.sleep(0.1)

class TaskApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.manager = TaskManager()
        await self.view.dock(self.manager)

if __name__ == "__main__":
    app = TaskApp()
    app.run()
