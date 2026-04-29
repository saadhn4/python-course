import random

options = ["rock", "paper", "scissors"]

computer_move = random.choice(options)

while True:
    player_move = input("Enter your move (q to exit): ")

    if player_move == "q":
        break

    if (
        not player_move == "rock"
        and not player_move == "paper"
        and not player_move == "scissors"
    ):
        print("Not a valid move")

    print(f"You picked {player_move}")
    print(f"Computer picked {computer_move}")

    if computer_move == "rock":
        if player_move == "rock":
            print("Tie!")
        if player_move == "paper":
            print("You win!")
        if player_move == "scissors":
            print("You lose!")

    if computer_move == "paper":
        if player_move == "rock":
            print("You lose!")
        if player_move == "paper":
            print("Tie")
        if player_move == "scissors":
            print("You win!")

    if computer_move == "scissors":
        if player_move == "rock":
            print("You win!")
        if player_move == "paper":
            print("You lose!")
        if player_move == "scissors":
            print("Tie")
