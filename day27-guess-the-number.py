# Guess the number

import random

lowest = int(input("Enter starting range: "))
highest = int(input("Enter ending range: "))
guesses = 0

number = random.randint(lowest, highest)

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess > highest or guess < lowest:
        print("That guess is out of range")
    elif guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed correct!")
        print(f"It took you {guesses} tries.")
        break
