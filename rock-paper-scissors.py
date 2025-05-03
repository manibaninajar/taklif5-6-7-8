import random

choices = ["rock", "paper", "scissors"]
user = input("Rock, paper, or scissors? ")

# check that the input is correct
if user not in choices:
    print("Invalid choice! You can only choose rock, paper, or scissors.")
else:
    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
