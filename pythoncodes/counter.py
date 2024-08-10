from textual.app import App
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Footer, Button, Label, Static
from rich.text import Text

class Counter(Static):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        self.label_text = label
        self.count = 0
        self.label = Label(f"{label}: {self.count}")
        self.increment_button = Button("+", id="increment-button")
        self.decrement_button = Button("-", id="decrement-button")
        self.reset_button = Button("Reset", id="reset-button")
        self.compose()

    def compose(self):
        self.update(Container(self.label, self.increment_button, self.decrement_button, self.reset_button, id="counter-container"))

    def increment(self):
        self.count += 1
        self.update_label()

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        self.update_label()

    def reset(self):
        self.count = 0
        self.update_label()

    def update_label(self):
        self.label.update(f"{self.label_text}: {self.count}")

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "increment-button":
            self.increment()
        elif button.id == "decrement-button":
            self.decrement()
        elif button.id == "reset-button":
            self.reset()

class CounterApp(App):
    CSS_PATH = "counter.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.counter_list = VerticalScroll(id="counter-list")
        self.add_counter_button = Button("Add Counter", id="add-counter-button")
        yield Container(self.add_counter_button, id="input-container")
        yield self.counter_list

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "add-counter-button":
            self.add_counter()

    def add_counter(self):
        counter_name = f"Counter {len(self.counter_list.children) + 1}"
        counter = Counter(counter_name)
        self.counter_list.mount(counter)

if __name__ == "__main__":
    CounterApp().run()