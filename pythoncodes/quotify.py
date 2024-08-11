import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

class QuoteGenerator:
    def __init__(self):
        self.console = Console()
        self.saved_quotes = []

    def fetch_quote(self):
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["content"], data["author"]
        else:
            return None, None

    def display_quote(self, quote, author):
        quote_text = Text(f'"{quote}"', style="bold cyan")
        author_text = Text(f"- {author}", style="bold yellow")
        panel = Panel(quote_text, title=author_text, border_style="green")
        self.console.print(panel)

    def save_quote(self, quote, author):
        self.saved_quotes.append((quote, author))
        self.console.print("Quote saved!", style="bold green")

    def view_saved_quotes(self):
        if not self.saved_quotes:
            self.console.print("No saved quotes yet.", style="bold yellow")
            return

        table = Table(title="Saved Quotes", box="ROUNDED")
        table.add_column("Quote", style="cyan", justify="left")
        table.add_column("Author", style="magenta", justify="left")

        for quote, author in self.saved_quotes:
            table.add_row(quote, author)

        self.console.print(table)

    def run(self):
        while True:
            self.console.print("\n[1] Get Random Quote  [2] View Saved Quotes  [3] Exit", style="bold magenta")
            choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="1")

            if choice == "1":
                quote, author = self.fetch_quote()
                if quote:
                    self.display_quote(quote, author)
                    if Confirm.ask("Would you like to save this quote?", default=False):
                        self.save_quote(quote, author)
                else:
                    self.console.print("Failed to fetch a quote. Please try again.", style="bold red")

            elif choice == "2":
                self.view_saved_quotes()

            elif choice == "3":
                self.console.print("Goodbye!", style="bold green")
                break

if __name__ == "__main__":
    app = QuoteGenerator()
    app.run()
