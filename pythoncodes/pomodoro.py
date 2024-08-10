from textual.app import App
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Label
from textual.timer import Timer
import time

class PomodoroTimerApp(App):
    CSS_PATH = "pomodoro.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.state = "stopped"
        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self.current_time = self.work_duration
        self.timer_label = Label(self.format_time(self.current_time), id="timer-label")
        self.status_label = Label("Ready to work?", id="status-label")
        self.start_button = Button("Start", id="start-button")
        self.stop_button = Button("Stop", id="stop-button")
        self.reset_button = Button("Reset", id="reset-button")
        yield Container(self.timer_label, self.status_label, self.start_button, self.stop_button, self.reset_button, id="main-container")

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.state == "running":
            if self.current_time > 0:
                self.current_time -= 1
                self.timer_label.update(self.format_time(self.current_time))
            else:
                self.state = "break" if self.state == "work" else "work"
                self.current_time = self.break_duration if self.state == "break" else self.work_duration
                self.status_label.update("Break Time!" if self.state == "break" else "Work Time!")
                self.timer_label.update(self.format_time(self.current_time))

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "start-button":
            self.start_timer()
        elif button.id == "stop-button":
            self.stop_timer()
        elif button.id == "reset-button":
            self.reset_timer()

    def start_timer(self):
        if self.state == "stopped":
            self.state = "work"
            self.status_label.update("Work Time!")
        if not hasattr(self, 'timer'):
            self.timer = Timer(self.update_timer, 1.0, repeat=True)
            self.mount(self.timer)
        self.timer.start()

    def stop_timer(self):
        if hasattr(self, 'timer'):
            self.timer.stop()

    def reset_timer(self):
        self.stop_timer()
        self.state = "stopped"
        self.current_time = self.work_duration
        self.timer_label.update(self.format_time(self.current_time))
        self.status_label.update("Ready to work?")

if __name__ == "__main__":
    PomodoroTimerApp().run()