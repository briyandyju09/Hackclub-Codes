from textual.app import App
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Label, Input
import random

class GuessingGame(App):
    CSS_PATH = "game.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.start_new_game()
        self.input = Input(placeholder="Enter your guess", id="guess-input")
        self.label = Label("Guess a number between 1 and 100", id="main-label")
        self.result_label = Label("", id="result-label")
        self.tries_label = Label("Attempts: 0", id="tries-label")
        self.new_game_button = Button("New Game", id="new-game-button")
        self.quit_button = Button("Quit", id="quit-button")
        yield Container(self.label, self.input, self.result_label, self.tries_label, self.new_game_button, self.quit_button, id="main-container")

    def start_new_game(self):
        self.number = random.randint(1, 100)
        self.tries = 0
        self.update_labels("Guess a number between 1 and 100", "", f"Attempts: {self.tries}")

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "new-game-button":
            self.start_new_game()
            self.input.focus()
        elif button.id == "quit-button":
            self.exit()
    
    def update_labels(self, main_text, result_text, tries_text):
        self.label.update(main_text)
        self.result_label.update(result_text)
        self.tries_label.update(tries_text)

    def on_input_submitted(self, event):
        guess = event.value.strip()
        if not guess.isdigit():
            self.result_label.update("Invalid input! Please enter a number.")
            return
        guess = int(guess)
        self.tries += 1
        if guess < self.number:
            self.update_labels("", "Too low!", f"Attempts: {self.tries}")
        elif guess > self.number:
            self.update_labels("", "Too high!", f"Attempts: {self.tries}")
        else:
            self.update_labels("Congratulations!", f"You guessed the number {self.number} correctly!", f"Attempts: {self.tries}")
        self.input.update("")

    def on_mount(self):
        self.input.focus()

if __name__ == "__main__":
    GuessingGame().run()