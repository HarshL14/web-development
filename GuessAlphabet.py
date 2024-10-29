import random
import string

def guess_alphabet():
    # Generate a random letter between 'a' and 'z'
    alphabet_to_guess = random.choice(string.ascii_lowercase)
    attempts = 0
    guess = None

    print("Welcome to the Alphabet Guessing Game!")
    print("I'm thinking of a letter between 'a' and 'z'.")

    while guess != alphabet_to_guess:
        # Get the player's guess
        guess = input("Enter your guess: ").lower()
        attempts += 1

        if guess < alphabet_to_guess:
            print("Too early in the alphabet! Try again.")
        elif guess > alphabet_to_guess:
            print("Too late in the alphabet! Try again.")
        else:
            print(f"Congratulations! You've guessed the letter '{alphabet_to_guess}' in {attempts} attempts.")

# Run the game
guess_alphabet()
