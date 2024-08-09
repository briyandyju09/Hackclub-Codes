from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class ExpenseTracker(Widget):
    expenses = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.total_expense = 0

    def render(self):
        expense_list = "\n".join([f"{expense['item']}: ${expense['amount']}" for expense in self.expenses])
        return Vertical(
            Static("Expense Tracker"),
            Static(self.message),
            Static(expense_list if expense_list else "No expenses recorded."),
            Button(label="Add Expense", id="add"),
            Button(label="Remove Expense", id="remove"),
            Button(label="List Expenses", id="list"),
            Button(label="Total Expenses", id="total"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_expense()
        elif button_id == "remove":
            await self.remove_expense()
        elif button_id == "list":
            await self.list_expenses()
        elif button_id == "total":
            await self.calculate_total_expense()
        await self.refresh()

    async def add_expense(self):
        self.message = "Enter expense item and amount separated by a comma:"
        await self.refresh()
        item_amount = await self.ask_user_input()
        if item_amount:
            item, amount = item_amount.split(",")
            self.expenses.append({"item": item.strip(), "amount": float(amount.strip())})
            self.message = f"Added expense: {item.strip()} - ${amount.strip()}"

    async def remove_expense(self):
        self.message = "Enter expense item to remove:"
        await self.refresh()
        item = await self.ask_user_input()
        self.expenses = [expense for expense in self.expenses if expense["item"] != item.strip()]
        self.message = f"Removed expense: {item.strip()}"

    async def list_expenses(self):
        self.message = "Listing all expenses:"

    async def calculate_total_expense(self):
        self.total_expense = sum(expense['amount'] for expense in self.expenses)
        self.message = f"Total Expenses: ${self.total_expense:.2f}"

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
          

class ExpenseTrackerApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")
      

    async def on_mount(self, event):
        self.tracker = ExpenseTracker()
        await self.view.dock(self.tracker)
      

if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.run()
