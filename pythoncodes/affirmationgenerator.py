import random
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

class AffirmationsGenerator:
    def __init__(self):
        self.console = Console()
        self.default_affirmations = [
            "I am capable of achieving great things.",
            "Every day is a new opportunity to grow.",
            "I am in charge of how I feel today.",
            "I believe in myself and my abilities.",
            "I am worthy of love and respect.",
            "I am resilient, strong, and brave.",
            "I can overcome any challenge that comes my way.",
            "I am a magnet for positivity and good vibes.",
            "I trust the process of life.",
            "I am becoming the best version of myself."
        ]
        self.custom_affirmations = []
        self.saved_affirmations = []

    def get_random_affirmation(self):
        all_affirmations = self.default_affirmations + self.custom_affirmations
        return random.choice(all_affirmations)

    def display_affirmation(self, affirmation):
        affirmation_text = Text(affirmation, style="bold cyan")
        panel = Panel(affirmation_text, title="Daily Affirmation", border_style="green")
        self.console.print(panel)

    def save_affirmation(self, affirmation):
        self.saved_affirmations.append(affirmation)
        self.console.print("Affirmation saved!", style="bold green")

    def view_saved_affirmations(self):
        if not self.saved_affirmations:
            self.console.print("No saved affirmations yet.", style="bold yellow")
            return

        table = Table(title="Saved Affirmations", box="ROUNDED")
        table.add_column("Affirmation", style="cyan")

        for affirmation in self.saved_affirmations:
            table.add_row(affirmation)

        self.console.print(table)

    def add_custom_affirmation(self):
        custom_affirmation = Prompt.ask("Enter your custom affirmation")
        self.custom_affirmations.append(custom_affirmation)
        self.console.print("Custom affirmation added!", style="bold green")

    def run(self):
        while True:
            self.console.print("\n[1] Get Daily Affirmation  [2] View Saved Affirmations  [3] Add Custom Affirmation  [4] Exit", style="bold magenta")
            choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"], default="1")

            if choice == "1":
                affirmation = self.get_random_affirmation()
                self.display_affirmation(affirmation)
                if Prompt.ask("Would you like to save this affirmation?", default="n").lower().startswith("y"):
                    self.save_affirmation(affirmation)

            elif choice == "2":
                self.view_saved_affirmations()

            elif choice == "3":
                self.add_custom_affirmation()

            elif choice == "4":
                self.console.print("Stay positive! Goodbye!", style="bold green")
                break

if __name__ == "__main__":
    app = AffirmationsGenerator()
    app.run()
