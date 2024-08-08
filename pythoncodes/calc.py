from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

console = Console()
history = []


def print_history():
    if not history:
        console.print(Panel("No history available.", style="red"))
        return
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Expression", min_width=30)
    table.add_column("Result", min_width=20)
    table.add_column("Date", min_width=20)

    for expr, result, date in history:
        table.add_row(expr, str(result), date)
    
    console.print(table)


def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"


def add_to_history(expression, result):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history.append((expression, result, date))


def calculate():
    expression = Prompt.ask("Enter the expression (e.g., 2 + 2)")
    result = evaluate_expression(expression)
    add_to_history(expression, result)
    console.print(Panel(f"Result: {result}", style="green"))


def view_history():
    print_history()


def exit_program():
    console.print(Panel("Goodbye!", style="bold green"))


def display_menu():
    console.print(Panel("Simple Calculator", style="bold blue"))
    console.print("[1] Calculate")
    console.print("[2] View History")
    console.print("[3] Exit")


def main():
    while True:
        display_menu()
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="3")

        if choice == "1":
            calculate()
        elif choice == "2":
            view_history()
        elif choice == "3":
            exit_program()
            break

if __name__ == "__main__":
    main()
