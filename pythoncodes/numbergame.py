import random


class NumberGuessingGame:
    def __init__(self):
        self.min_range = 1
        self.max_range = 100
        self.attempts = 10
        self.play_game()

  
    def generate_number(self):
        return random.randint(self.min_range, self.max_range)


    def get_feedback(self, guess, number):
        if guess < number:
            return "Too low!"
        elif guess > number:
            return "Too high!"
        else:
            return "Correct!"


  
    def play_game(self):
        while True:
            number = self.generate_number()
            print(f"Guess the number between {self.min_range} and {self.max_range}. You have {self.attempts} attempts.")
            success = False

            for attempt in range(self.attempts):
                try:
                    guess = int(input(f"Attempt {attempt + 1}: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")

                    continue

                feedback = self.get_feedback(guess, number)
                print(feedback)

                if feedback == "Correct!":
                    success = True
                  
                    break


          
            if success:
                print("Congratulations! You guessed the number.")
                self.min_range -= 5
                self.max_range += 5
                self.attempts += 1
              
            else:
                print(f"Sorry! The correct number was {number}.")
                self.min_range += 5
                self.max_range -= 5
                self.attempts = max(1, self.attempts - 1)

            if self.min_range < 1:
                self.min_range = 1
            if self.max_range > 1000:
                self.max_range = 1000

          
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
          
            if play_again != "yes":
                print("Thank you for playing!")
                break


if __name__ == "__main__":
  
    NumberGuessingGame()
