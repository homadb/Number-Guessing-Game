import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! try guessing higher.")
        elif guess > target_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulation! You guessed the number {target_number} in {attempts}.")
            break

guess_number()