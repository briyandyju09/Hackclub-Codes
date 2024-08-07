class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Description: {self.description}, Amount: ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.run()

    def add_expense(self):
        description = input("Enter expense description: ").strip()
        try:
            amount = float(input("Enter expense amount: ").strip())
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        expense = Expense(description, amount)
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses available.")
        else:
            for i, expense in enumerate(self.expenses):
                print(f"{i+1}. {expense}")

    def update_expense(self):
        self.view_expenses()
        if not self.expenses:
            return
        try:
            index = int(input("Enter the number of the expense to update: ")) - 1
            if 0 <= index < len(self.expenses):
                expense = self.expenses[index]
                expense.description = input(f"Enter new description (current: {expense.description}): ").strip()
                try:
                    expense.amount = float(input(f"Enter new amount (current: {expense.amount}): ").strip())
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    return
                print(f"Updated expense: {expense}")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_expense(self):
        self.view_expenses()
        if not self.expenses:
            return
        try:
            index = int(input("Enter the number of the expense to delete: ")) - 1
            if 0 <= index < len(self.expenses):
                expense = self.expenses.pop(index)
                print(f"Deleted expense: {expense}")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}")

    def calculate_average_expense(self):
        if not self.expenses:
            print("No expenses available to calculate average.")
        else:
            total = sum(expense.amount for expense in self.expenses)
            average = total / len(self.expenses)
            print(f"Average expense: ${average:.2f}")

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Calculate Total Expenses")
            print("6. Calculate Average Expense")
            print("7. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.update_expense()
            elif choice == '4':
                self.delete_expense()
            elif choice == '5':
                self.calculate_total_expenses()
            elif choice == '6':
                self.calculate_average_expense()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    ExpenseTracker()