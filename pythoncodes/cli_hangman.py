import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = []
        self.guessed_word = ['_'] * len(self.word)
        self.attempts = 6
        self.hints_used = 0
        self.max_hints = 3
        self.run()

    def display_state(self):
        print("\nCurrent State:")
        print(f"Word: {' '.join(self.guessed_word)}")
        print(f"Guessed letters: {', '.join(self.guessed_letters)}")
        print(f"Attempts remaining: {self.attempts}")
        print(f"Hints used: {self.hints_used}/{self.max_hints}\n")

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return

        self.guessed_letters.append(letter)
        if letter in self.word:
            print(f"Good guess! {letter} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed_word[i] = letter
        else:
            print(f"Sorry, {letter} is not in the word.")
            self.attempts -= 1

    def use_hint(self):
        if self.hints_used >= self.max_hints:
            print("No more hints available.")
            return

        hint_letter = random.choice([c for c in self.word if c not in self.guessed_word])
        self.hints_used += 1
        print(f"Hint: The word contains the letter '{hint_letter}'.")
        self.guess(hint_letter)

    def check_win(self):
        return '_' not in self.guessed_word

    def run(self):
        print("Welcome to Hangman!")
        while self.attempts > 0:
            self.display_state()
            action = input("Choose an action - (G)uess a letter, (H)int, or (Q)uit: ").strip().upper()
            if action == 'G':
                guess = input("Guess a letter: ").strip().upper()
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single letter.")
                    continue
                self.guess(guess)
            elif action == 'H':
                self.use_hint()
            elif action == 'Q':
                print("Goodbye!")
                break
            else:
                print("Invalid action. Please choose G, H, or Q.")
            if self.check_win():
                print(f"Congratulations! You guessed the word: {self.word}")
                break
        else:
            print(f"Game over! The word was: {self.word}")

if __name__ == '__main__':
    words = ["PYTHON", "DEVELOPER", "HANGMAN", "CHALLENGE", "PROGRAMMING","ARCADE","CODE"]
    Hangman(words)