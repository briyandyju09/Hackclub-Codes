import json
import os

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)
        self.load()

    def load(self):
        with open(self.filename, "r") as f:
            self.expenses = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, description, amount):
        expense = {"description": description, "amount": amount}
        self.expenses.append(expense)
        self.save()
        print(f"Expense added: {description} - ${amount:.2f}")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        return total

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for expense in self.expenses:
            print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. List All Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)

        elif choice == "2":
            total = tracker.total_expenses()
            print(f"Total Expenses: ${total:.2f}")

        elif choice == "3":
            tracker.list_expenses()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
