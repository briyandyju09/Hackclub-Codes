from datetime import datetime
from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class HabitTracker(Widget):
    habits = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.current_habits = []

    def render(self):
        habit_list = "\n".join([f"{habit['name']} - {habit['streak']} days streak" for habit in self.current_habits])
        return Vertical(
            Static("Habit Tracker"),
            Static(self.message),
            Static(habit_list if habit_list else "No habits tracked."),
            Button(label="Add Habit", id="add"),
            Button(label="Mark Habit Complete", id="complete"),
            Button(label="View Habit Progress", id="progress"),
            Button(label="List All Habits", id="list"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_habit()
        elif button_id == "complete":
            await self.mark_habit_complete()
        elif button_id == "progress":
            await self.view_habit_progress()
        elif button_id == "list":
            await self.list_all_habits()
        await self.refresh()

    async def add_habit(self):
        self.message = "Enter the habit name to track:"
        await self.refresh()
        habit_name = await self.ask_user_input()
        if habit_name:
            self.habits.append({"name": habit_name.strip(), "streak": 0, "last_completed": None})
            self.message = f"Added habit: {habit_name.strip()}"

    async def mark_habit_complete(self):
        self.message = "Enter the habit name to mark as completed:"
        await self.refresh()
        habit_name = await self.ask_user_input()
        for habit in self.habits:
            if habit["name"] == habit_name.strip():
                today = datetime.now().date()
                if habit["last_completed"] != today:
                    habit["streak"] += 1
                    habit["last_completed"] = today
                    self.message = f"Marked '{habit_name.strip()}' as completed. Streak: {habit['streak']} days"
                else:
                    self.message = f"Habit '{habit_name.strip()}' is already completed for today."
                break
        else:
            self.message = f"Habit '{habit_name.strip()}' not found."

    async def view_habit_progress(self):
        self.message = "Enter the habit name to view progress:"
        await self.refresh()
        habit_name = await self.ask_user_input()
        for habit in self.habits:
            if habit["name"] == habit_name.strip():
                self.current_habits = [habit]
                self.message = f"Progress of '{habit_name.strip()}': {habit['streak']} days streak"
                break
        else:
            self.message = f"Habit '{habit_name.strip()}' not found."

    async def list_all_habits(self):
        self.current_habits = self.habits
        self.message = "Listing all tracked habits:"

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

class HabitTrackerApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.tracker = HabitTracker()
        await self.view.dock(self.tracker)

if __name__ == "__main__":
    app = HabitTrackerApp()
    app.run()
