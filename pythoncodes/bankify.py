from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, Static, Header, Footer
from textual.containers import Vertical, Horizontal
from textual.screen import Screen

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, amount, target_account):
        if amount > self.balance:
            return False
        self.balance -= amount
        target_account.balance += amount
        return True

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: ${self.balance:.2f}"

class BankingApp(App):
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
        self.accounts = {}
        self.current_account = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Banking System"),
            Button("Create Account", id="create"),
            Button("Deposit Money", id="deposit"),
            Button("Withdraw Money", id="withdraw"),
            Button("Transfer Money", id="transfer"),
            Button("Check Balance", id="check_balance"),
            Button("Exit", id="exit"),
            id="menu"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "create":
            self.push_screen(CreateAccountScreen(self))
        elif button_id == "deposit":
            self.push_screen(DepositScreen(self))
        elif button_id == "withdraw":
            self.push_screen(WithdrawScreen(self))
        elif button_id == "transfer":
            self.push_screen(TransferScreen(self))
        elif button_id == "check_balance":
            self.push_screen(CheckBalanceScreen(self))
        elif button_id == "exit":
            self.exit()

    def create_account(self, account_number, name, initial_deposit):
        self.accounts[account_number] = Account(account_number, name, initial_deposit)

class CreateAccountScreen(Screen):
    def __init__(self, app: BankingApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Create Account"),
            Input(placeholder="Account Number", id="account_number"),
            Input(placeholder="Name", id="name"),
            Input(placeholder="Initial Deposit", id="initial_deposit"),
            Button("Create", id="create"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create":
            account_number = self.query_one("#account_number", Input).value
            name = self.query_one("#name", Input).value
            initial_deposit = float(self.query_one("#initial_deposit", Input).value)
            self.app.create_account(account_number, name, initial_deposit)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class DepositScreen(Screen):
    def __init__(self, app: BankingApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Deposit Money"),
            Input(placeholder="Account Number", id="account_number"),
            Input(placeholder="Amount", id="amount"),
            Button("Deposit", id="deposit"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "deposit":
            account_number = self.query_one("#account_number", Input).value
            amount = float(self.query_one("#amount", Input).value)
            account = self.app.accounts.get(account_number)
            if account:
                account.deposit(amount)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class WithdrawScreen(Screen):
    def __init__(self, app: BankingApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Withdraw Money"),
            Input(placeholder="Account Number", id="account_number"),
            Input(placeholder="Amount", id="amount"),
            Button("Withdraw", id="withdraw"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "withdraw":
            account_number = self.query_one("#account_number", Input).value
            amount = float(self.query_one("#amount", Input).value)
            account = self.app.accounts.get(account_number)
            if account:
                account.withdraw(amount)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class TransferScreen(Screen):
    def __init__(self, app: BankingApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Transfer Money"),
            Input(placeholder="From Account Number", id="from_account"),
            Input(placeholder="To Account Number", id="to_account"),
            Input(placeholder="Amount", id="amount"),
            Button("Transfer", id="transfer"),
            Button("Back", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "transfer":
            from_account_number = self.query_one("#from_account", Input).value
            to_account_number = self.query_one("#to_account", Input).value
            amount = float(self.query_one("#amount", Input).value)
            from_account = self.app.accounts.get(from_account_number)
            to_account = self.app.accounts.get(to_account_number)
            if from_account and to_account:
                from_account.transfer(amount, to_account)
            self.app.pop_screen()
        elif event.button.id == "back":
            self.app.pop_screen()

class CheckBalanceScreen(Screen):
    def __init__(self, app: BankingApp):
        super().__init__()
        self.app = app

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Check Balance"),
            Input(placeholder="Account Number", id="account_number"),
            Button("Check", id="check"),
            Button("Back", id="back"),
            Static(id="balance_output"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "check":
            account_number = self.query_one("#account_number", Input).value
            account = self.app.accounts.get(account_number)
            output = self.query_one("#balance_output", Static)
            if account:
                output.update(f"Current balance: ${account.balance:.2f}")
            else:
                output.update("Account not found.")
        elif event.button.id == "back":
            self.app.pop_screen()

if __name__ == "__main__":
    BankingApp().run()