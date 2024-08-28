import random

class BettingPlatform:
    def __init__(self):
        self.points = 5
        self.match_outcomes = ["Team A wins", "Team B wins", "Draw"]
        self.current_bet = None
        self.bet_amount = 0

    def place_bet(self):
        print("\nAvailable bets:")
        for i, outcome in enumerate(self.match_outcomes, 1):
            print(f"{i}. {outcome}")
        
        bet_choice = int(input("Choose your bet (1-3): ")) - 1
        if bet_choice not in range(3):
            print("Invalid choice.")
            return False
        
        bet_amount = int(input(f"Enter your bet amount (Available points: {self.points}): "))
        if bet_amount <= 0 or bet_amount > self.points:
            print("Invalid bet amount.")
            return False
        
        self.current_bet = self.match_outcomes[bet_choice]
        self.bet_amount = bet_amount
        self.points -= bet_amount
        print(f"Bet placed: {self.current_bet} with {self.bet_amount} points.")
        return True

    def resolve_bet(self):
        outcome = random.choice(self.match_outcomes)
        print(f"\nMatch outcome: {outcome}")
        if outcome == self.current_bet:
            self.points += self.bet_amount * 2
            print(f"You won! Your new points total: {self.points}")
        else:
            print(f"You lost. Your new points total: {self.points}")
        self.current_bet = None
        self.bet_amount = 0

    def view_points(self):
        print(f"\nYour current points: {self.points}")

def main():
    platform = BettingPlatform()

    while True:
        print("\nBetting Platform")
        print("1. Place Bet")
        print("2. View Points")
        print("3. Resolve Bet")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            platform.place_bet()

        elif choice == "2":
            platform.view_points()

        elif choice == "3":
            if platform.current_bet is None:
                print("No bet placed. Place a bet first.")
            else:
                platform.resolve_bet()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
