import random

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self, holder_name):
        account_number = self.next_account_number
        self.next_account_number += 1
        self.accounts[account_number] = BankAccount(account_number, holder_name)
        print(f"Account created for {holder_name} with account number {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account and account.deposit(amount):
            print(f"Deposited ${amount:.2f} into account number {account_number}")
        else:
            print("Deposit failed. Check account number and amount.")

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account and account.withdraw(amount):
            print(f"Withdrew ${amount:.2f} from account number {account_number}")
        else:
            print("Withdrawal failed. Check account number and amount.")

    def view_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Balance for account number {account_number}: ${account.get_balance():.2f}")
        else:
            print("Account not found.")

    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        for account in self.accounts.values():
            print(account)

def main():
    bank = BankSystem()
    
    while True:
        print("\nBank System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. List All Accounts")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            holder_name = input("Enter account holder's name: ")
            bank.create_account(holder_name)

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter account number: "))
            bank.view_balance(account_number)

        elif choice == "5":
            bank.list_accounts()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
