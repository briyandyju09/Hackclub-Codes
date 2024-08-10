from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, Static, Header, Footer
from textual.containers import Vertical, Horizontal
from textual.screen import Screen

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.description} - ${self.amount:.2f} [{self.category}]"

class ExpenseTrackerApp(App):
    CSS = """
    Vertical {
        border: round #333;
        padding: 2;
        margin: 1;
        background: #111;
    }
    """

    def __init__(self):
        super().__init__()
        self.expenses = []

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Expense Tracker"),
            Button("Add Expense", id="add_expense"),
            Button("View Expenses", id="view_expenses"),
            Button("Reset Expenses", id="reset_expenses"),
            Button("Exit", id="exit"),
            id="menu"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "add_expense":
            self.push_screen(AddExpenseScreen(self))
        elif button_id == "view_expenses":
            self.push_screen(ViewExpensesScreen(self))
        elif button_id == "reset_expenses":
            self.expenses = []
        elif button_id == "exit":
            self.exit()

    def add_expense(self, description, amount, category):
        self.expenses.append(Expense(description, amount, category))

class AddExpenseScreen(Screen):
    def __init__(self, app: ExpenseTrackerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add Expense"),
            Input(placeholder="Description", id="description"),
            Input(placeholder="Amount", id="amount"),
            Input(placeholder="Category", id="category"),
            Button("Add", id="add"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            description = self.query_one("#description", Input).value
            amount = float(self.query_one("#amount", Input).value)
            category = self.query_one("#category", Input).value
            self.app.add_expense(description, amount, category)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class ViewExpensesScreen(Screen):
    def __init__(self, app: ExpenseTrackerApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("View Expenses"),
            Button("Back", id="back"),
            Static(id="expenses_output"),
        )

    def on_screen_opened(self) -> None:
        output = self.query_one("#expenses_output", Static)
        total_expense = sum(expense.amount for expense in self.app.expenses)
        expense_list = "\n".join(str(expense) for expense in self.app.expenses)
        output.update(f"{expense_list}\n\nTotal Expense: ${total_expense:.2f}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

if __name__ == "__main__":
    ExpenseTrackerApp().run()