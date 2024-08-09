from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class FitnessTracker(Widget):
    exercises = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.current_view = ""

    def render(self):
        exercise_list = "\n".join([f"{idx + 1}. {exercise['name']} - {exercise['duration']} min - {exercise['calories']} kcal" for idx, exercise in enumerate(self.exercises)])
        return Vertical(
            Static("Fitness Tracker"),
            Static(self.message),
            Static(exercise_list if exercise_list else "No exercises logged."),
            Button(label="Log Exercise", id="log"),
            Button(label="View History", id="history"),
            Button(label="Total Calories Burned", id="calories"),
            Button(label="View Summary", id="summary"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "log":
            await self.log_exercise()
        elif button_id == "history":
            await self.view_history()
        elif button_id == "calories":
            await self.calculate_total_calories()
        elif button_id == "summary":
            await self.view_summary()
        await self.refresh()

    async def log_exercise(self):
        self.message = "Enter exercise name, duration (min), and calories burned separated by commas:"
        await self.refresh()
        exercise_info = await self.ask_user_input()
        if exercise_info:
            name, duration, calories = exercise_info.split(",")
            self.exercises.append({"name": name.strip(), "duration": int(duration.strip()), "calories": int(calories.strip())})
            self.message = f"Logged exercise: {name.strip()}"

    async def view_history(self):
        self.current_view = "history"
        self.message = "Exercise history:"

    async def calculate_total_calories(self):
        total_calories = sum(exercise['calories'] for exercise in self.exercises)
        self.message = f"Total calories burned: {total_calories} kcal"

    async def view_summary(self):
        total_exercises = len(self.exercises)
        total_duration = sum(exercise['duration'] for exercise in self.exercises)
        total_calories = sum(exercise['calories'] for exercise in self.exercises)
        self.message = f"Summary: {total_exercises} exercises, {total_duration} min, {total_calories} kcal"

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

class FitnessApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.tracker = FitnessTracker()
        await self.view.dock(self.tracker)

if __name__ == "__main__":
    app = FitnessApp()
    app.run()
