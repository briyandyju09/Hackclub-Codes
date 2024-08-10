from textual.app import App
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Footer, Button, Label, Static, Input
from random import shuffle

class Flashcard(Static):
    def __init__(self, question, answer, **kwargs):
        super().__init__(**kwargs)
        self.question = question
        self.answer = answer
        self.showing_answer = False
        self.question_label = Label(question)
        self.answer_label = Label("", visible=False)
        self.flip_button = Button("Show Answer", id="flip-button")
        self.compose()

    def compose(self):
        self.update(Container(self.question_label, self.answer_label, self.flip_button, id="flashcard-container"))

    def flip(self):
        if self.showing_answer:
            self.answer_label.update("")
            self.flip_button.update("Show Answer")
        else:
            self.answer_label.update(self.answer)
            self.flip_button.update("Show Question")
        self.showing_answer = not self.showing_answer
        self.answer_label.visible = self.showing_answer

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "flip-button":
            self.flip()

class FlashcardApp(App):
    CSS_PATH = "flashcard.css"

    def compose(self):
        yield Header()
        yield Footer()
        self.flashcards = []
        self.current_card_index = 0
        self.load_flashcards()
        self.flashcard_display = VerticalScroll(id="flashcard-display")
        self.next_button = Button("Next", id="next-button")
        self.prev_button = Button("Previous", id="prev-button")
        yield Container(self.flashcard_display, id="display-container")
        yield Container(self.prev_button, self.next_button, id="navigation-container")

    def load_flashcards(self):
        flashcards_data = [
            ("What is the capital of France?", "Paris"),
            ("What is 2 + 2?", "4"),
            ("What is the tallest mountain in the world?", "Mount Everest"),
            ("Who wrote '1984'?", "George Orwell"),
            ("What is the smallest prime number?", "2")
        ]
        shuffle(flashcards_data)
        for question, answer in flashcards_data:
            self.flashcards.append(Flashcard(question, answer))
        if self.flashcards:
            self.flashcard_display.mount(self.flashcards[0])

    def on_button_pressed(self, event):
        button = event.sender
        if button.id == "next-button":
            self.next_card()
        elif button.id == "prev-button":
            self.previous_card()

    def next_card(self):
        if self.current_card_index < len(self.flashcards) - 1:
            self.current_card_index += 1
            self.show_card()

    def previous_card(self):
        if self.current_card_index > 0:
            self.current_card_index -= 1
            self.show_card()

    def show_card(self):
        self.flashcard_display.clear()
        self.flashcard_display.mount(self.flashcards[self.current_card_index])

if __name__ == "__main__":
    FlashcardApp().run()