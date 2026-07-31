import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI chose a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            print("Choose a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f'Correct! You guess it in {attempts} attempts.')
            break


def main():
    print("=== Number Guessing Game ===")

    while True:
        play_game()

        answer = input("\nPlay again? (Yes/No): ").strip().lower()

        if answer != "yes":
            print("Game closed.")
            break

if __name__ == "__main__":
    main()


