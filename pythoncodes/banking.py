import json
import os


class BankingSystem:
    def __init__(self, filename='accounts.json'):
        self.filename = filename
        self.accounts = self.load_accounts()
        self.run()

    def load_accounts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error loading accounts file. File may be corrupted.")
                return {}
        return {}

  
    def save_accounts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.accounts, file, indent=4)
        except IOError:
            print("Error saving accounts to file.")

    def create_account(self, name):
        if not name:
            print("Account name cannot be empty.")
            return
        if name in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[name] = 0.0
            self.save_accounts()
            print(f"Account created: {name}")

    def deposit(self, name, amount):
        if name not in self.accounts:
            print("Account not found.")
        elif amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.accounts[name] += amount
            self.save_accounts()
            print(f"Deposited ${amount:.2f} into account: {name}")

    def withdraw(self, name, amount):
        if name not in self.accounts:
            print("Account not found.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.accounts[name] < amount:
            print("Insufficient funds.")
        else:
            self.accounts[name] -= amount
            self.save_accounts()
            print(f"Withdrew ${amount:.2f} from account: {name}")

  
    def view_balance(self, name):
        if name not in self.accounts:
            print("Account not found.")
        else:
            balance = self.accounts[name]
            print(f"Account: {name}, Balance: ${balance:.2f}")

    def run(self):
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Balance")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

          
            if choice == '1':
                name = input("Enter account name: ").strip()
                self.create_account(name)
            elif choice == '2':
                name = input("Enter account name: ").strip()
                amount = float(input("Enter deposit amount: ").strip())
                self.deposit(name, amount)
            elif choice == '3':
                name = input("Enter account name: ").strip()
                amount = float(input("Enter withdrawal amount: ").strip())
                self.withdraw(name, amount)
            elif choice == '4':
                name = input("Enter account name: ").strip()
                self.view_balance(name)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    BankingSystem()
