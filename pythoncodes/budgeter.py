from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class BudgetTracker(Widget):
    transactions = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balance = 0
        self.message = ""
        self.current_view = ""

    def render(self):
        transaction_list = "\n".join([f"{idx + 1}. {transaction['type']}: {transaction['amount']} - {transaction['description']}" for idx, transaction in enumerate(self.transactions)])
        return Vertical(
            Static("Personal Budget Tracker"),
            Static(f"Balance: ${self.balance:.2f}"),
            Static(self.message),
            Static(transaction_list if transaction_list else "No transactions recorded."),
            Button(label="Add Expense", id="expense"),
            Button(label="Add Income", id="income"),
            Button(label="View Summary", id="summary"),
            Button(label="View Transactions", id="transactions"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "expense":
            await self.add_expense()
        elif button_id == "income":
            await self.add_income()
        elif button_id == "summary":
            await self.view_summary()
        elif button_id == "transactions":
            await self.view_transactions()
        await self.refresh()

    async def add_expense(self):
        self.message = "Enter expense amount and description separated by a comma:"
        await self.refresh()
        expense_info = await self.ask_user_input()
        if expense_info:
            amount, description = expense_info.split(",", 1)
            self.transactions.append({"type": "Expense", "amount": -float(amount.strip()), "description": description.strip()})
            self.balance -= float(amount.strip())
            self.message = f"Added expense: ${amount.strip()} for {description.strip()}"

    async def add_income(self):
        self.message = "Enter income amount and description separated by a comma:"
        await self.refresh()
        income_info = await self.ask_user_input()
        if income_info:
            amount, description = income_info.split(",", 1)
            self.transactions.append({"type": "Income", "amount": float(amount.strip()), "description": description.strip()})
            self.balance += float(amount.strip())
            self.message = f"Added income: ${amount.strip()} from {description.strip()}"

    async def view_summary(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == "Income")
        total_expense = sum(-t['amount'] for t in self.transactions if t['type'] == "Expense")
        self.message = f"Summary: Total Income: ${total_income:.2f}, Total Expenses: ${total_expense:.2f}, Balance: ${self.balance:.2f}"

    async def view_transactions(self):
        self.message = "Viewing all transactions."

    async def ask_user_input(self):
        input_widget = Input()
        await self.view.dock(input_widget)
        input_widget.focus()
        await self.wait_for_input(input_widget)
        user_input = input_widget.value
        await input_widget.remove()
        return user_input

    async def wait_for_input(self, input_widget):
        while not input_widget.value:
            await self.sleep(0.1)

class BudgetApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.tracker = BudgetTracker()
        await self.view.dock(self.tracker)

if __name__ == "__main__":
    app = BudgetApp()
    app.run()