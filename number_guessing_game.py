import random


def play_guessing_game():
    print("================================")
    print("Welcome to the Number Guessing Game!")
    print("================================")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            response = input("\nEnter your guess (or type 'quit' to stop): ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\nThanks for playing! The secret number was {secret_number}.")
            return

        if response.lower() == "quit":
            print(f"Thanks for playing! The secret number was {secret_number}.")
            return

        try:
            guess = int(response)
        except ValueError:
            print("Please enter a whole number or 'quit'.")
            continue

        if not 1 <= guess <= 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            unit = "attempt" if attempts == 1 else "attempts"
            print(f"\nCongratulations! You guessed the number in {attempts} {unit}!")
            return


if __name__ == "__main__":
    play_guessing_game()
