from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Label, Header, Footer
import time

class PomodoroTimerApp(App):
    CSS_PATH = "pomodoro.css"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            self.timer_label := Label("25:00"),
            Button("Start", id="start"),
            Button("Pause", id="pause"),
            Button("Reset", id="reset"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "start":
            self.start_timer()
        elif button_id == "pause":
            self.pause_timer()
        elif button_id == "reset":
            self.reset_timer()

    def start_timer(self):
        self.paused = False
        self.time_remaining = 25 * 60 
        self.set_timer(self.time_remaining)
        self.refresh()

    def pause_timer(self):
        self.paused = True

    def reset_timer(self):
        self.paused = True
        self.time_remaining = 25 * 60 
        self.set_timer(self.time_remaining)
        self.refresh()

    def set_timer(self, seconds: int):
        minutes = seconds // 60
        seconds = seconds % 60
        self.timer_label.update(f"{minutes:02}:{seconds:02}")

    def on_mount(self):
        self.time_remaining = 25 * 60  
        self.paused = True
        self.set_interval(1, self.update_timer)

    def update_timer(self):
        if not self.paused and self.time_remaining > 0:
            self.time_remaining -= 1
            self.set_timer(self.time_remaining)
            if self.time_remaining == 0:
                self.timer_label.update("Time's up!")
                self.paused = True

if __name__ == "__main__":
    PomodoroTimerApp().run()
