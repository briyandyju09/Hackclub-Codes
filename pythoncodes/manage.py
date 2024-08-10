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

    def render(self):
        task_list = "\n".join([f"{idx + 1}. [{'X' if task['completed'] else ' '}] {task['description']}" for idx, task in enumerate(self.tasks)])
        return Vertical(
            Static("Task Manager"),
            Static(self.message),
            Static(task_list if task_list else "No tasks available."),
            Button(label="Add Task", id="add"),
            Button(label="Mark Task as Completed", id="complete"),
            Button(label="Delete Task", id="delete"),
            Button(label="View Tasks", id="view"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_task()
        elif button_id == "complete":
            await self.complete_task()
        elif button_id == "delete":
            await self.delete_task()
        elif button_id == "view":
            await self.view_tasks()
        await self.refresh()

    async def add_task(self):
        self.message = "Enter task description:"
        await self.refresh()
        task_description = await self.ask_user_input()
        if task_description:
            self.tasks.append({"description": task_description.strip(), "completed": False})
            self.message = f"Added task: {task_description.strip()}"

    async def complete_task(self):
        self.message = "Enter task number to mark as completed:"
        await self.refresh()
        task_number = await self.ask_user_input()
        if task_number and task_number.isdigit() and 0 < int(task_number) <= len(self.tasks):
            self.tasks[int(task_number) - 1]["completed"] = True
            self.message = f"Marked task {task_number} as completed."

    async def delete_task(self):
        self.message = "Enter task number to delete:"
        await self.refresh()
        task_number = await self.ask_user_input()
        if task_number and task_number.isdigit() and 0 < int(task_number) <= len(self.tasks):
            deleted_task = self.tasks.pop(int(task_number) - 1)
            self.message = f"Deleted task: {deleted_task['description']}"

    async def view_tasks(self):
        self.message = "Viewing all tasks."

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