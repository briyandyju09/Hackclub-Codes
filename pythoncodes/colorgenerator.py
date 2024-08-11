import random
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

class ColorGenerator:
    def __init__(self):
        self.console = Console()
        self.saved_colors = []

    def generate_random_color(self):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        return color

    def display_color(self, color):
        color_text = Text(f"Color: {color}", style=f"bold {color}")
        panel = Panel(color_text, title="Random Color", border_style=f"{color}")
        self.console.print(panel)

    def save_color(self, color):
        self.saved_colors.append(color)
        self.console.print(f"Color {color} saved!", style=f"bold {color}")

    def view_saved_colors(self):
        if not self.saved_colors:
            self.console.print("No saved colors yet.", style="bold yellow")
            return

        table = Table(title="Saved Colors", box="ROUNDED")
        table.add_column("Color Code", style="cyan", justify="center")
        table.add_column("Color", style="bold", justify="center")

        for color in self.saved_colors:
            table.add_row(color, f"[{color}]{color}[/{color}]")

        self.console.print(table)

    def run(self):
        while True:
            self.console.print("\n[1] Generate Random Color  [2] View Saved Colors  [3] Exit", style="bold magenta")
            choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="1")

            if choice == "1":
                color = self.generate_random_color()
                self.display_color(color)
                if Prompt.ask("Would you like to save this color?", default="n").lower().startswith("y"):
                    self.save_color(color)

            elif choice == "2":
                self.view_saved_colors()

            elif choice == "3":
                self.console.print("Goodbye!", style="bold green")
                break

if __name__ == "__main__":
    app = ColorGenerator()
    app.run()
