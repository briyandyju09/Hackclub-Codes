class Expense:
    def __init__(self, description, amount, participants):
        self.description = description
        self.amount = amount
        self.participants = participants

    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}, Participants: {', '.join(self.participants)}"

class ExpenseSplitter:
    def __init__(self):
        self.expenses = []
        self.run()

    def add_expense(self):
        description = input("Enter the expense description: ").strip()
        try:
            amount = float(input("Enter the amount: ").strip())
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        participants = input("Enter participants (comma-separated): ").strip().split(',')
        participants = [p.strip() for p in participants]
        self.expenses.append(Expense(description, amount, participants))
        print(f"Added: {self.expenses[-1]}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for idx, expense in enumerate(self.expenses, 1):
                print(f"{idx}. {expense}")

    def calculate_split(self):
        if not self.expenses:
            print("No expenses to split.")
            return
        
        total_per_person = {}
        for expense in self.expenses:
            split_amount = expense.amount / len(expense.participants)
            for person in expense.participants:
                if person in total_per_person:
                    total_per_person[person] += split_amount
                else:
                    total_per_person[person] = split_amount

        print("Amount each person owes:")
        for person, amount in total_per_person.items():
            print(f"{person}: ${amount:.2f}")

    def delete_expense(self):
        self.view_expenses()
        try:
            index = int(input("Enter the number of the expense to delete: ")) - 1
            if 0 <= index < len(self.expenses):
                deleted_expense = self.expenses.pop(index)
                print(f"Deleted: {deleted_expense}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            print("\nExpense Splitter Menu")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Calculate Split")
            print("4. Delete Expense")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.calculate_split()
            elif choice == '4':
                self.delete_expense()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    ExpenseSplitter()