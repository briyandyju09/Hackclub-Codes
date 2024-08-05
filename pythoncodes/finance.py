import json
import os
from datetime import datetime, timedelta

DATA_FILE = 'expenses.json'
REPORT_FILE = 'monthly_summary.txt'

def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump({"expenses": []}, file)
        print("Initialized expense data file.")

def add_expense(amount, category, description=""):
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().isoformat()
        }
        
        data["expenses"].append(expense)
        
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Added expense: ${amount} for {category}.")
    except Exception as e:
        print(f"Error adding expense: {e}")

def view_today_expenses():
    today = datetime.now().date()
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        
        today_expenses = [e for e in data["expenses"] 
                          if datetime.fromisoformat(e["date"]).date() == today]
        
        if today_expenses:
            print(f"Expenses for {today}:")
            for expense in today_expenses:
                print(f"  ${expense['amount']:.2f} - {expense['category']}: {expense['description']}")
        else:
            print("No expenses recorded for today.")
    except Exception as e:
        print(f"Error viewing today's expenses: {e}")

def generate_monthly_report():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        
        monthly_expenses = {}
        for expense in data["expenses"]:
            date = datetime.fromisoformat(expense["date"])
            month = date.strftime("%Y-%m")
            if month not in monthly_expenses:
                monthly_expenses[month] = 0
            monthly_expenses[month] += expense["amount"]
        
        with open(REPORT_FILE, 'w') as file:
            for month, total in monthly_expenses.items():
                file.write(f"{month}: ${total:.2f}\n")
        
        print(f"Monthly summary report generated in {REPORT_FILE}.")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    initialize_data_file()
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. View Today's Expenses")
        print("3. Generate Monthly Report")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_today_expenses()
        elif choice == '3':
            generate_monthly_report()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()