
#Rock Paper Scissors exercise using python
import random

#Setting up the 3 options
CHOICES = ["rock", "paper", "scissors"]

#Establishing all other variables in order to shorten code
loser = "\nYou Lose :("
winner = "\nYOU WIN!"
tied = "\nIt's a Tie"
user_choice = input("   Type rock, paper, or scissors\n")
computer_choice = random.choice(CHOICES)
whatThrow = f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'"

#Starting the function to determine winner based on if statements
#IF TIED
if user_choice == computer_choice:
    print(whatThrow)
    print(tied)
#IF ROCK
elif user_choice == "rock":
    if computer_choice == "scissors":
        print(whatThrow)
        print("Rock crushes scissors")
        print(winner)
    else:
        print(whatThrow)
        print("Paper covers Rock")
        print(loser)
#IF SCISSORS
elif user_choice == "scissors":
    if computer_choice == "paper":
        print(whatThrow)
        print("Scissors cuts Paper")
        print(winner)
    elif computer_choice == "rock":
        print(whatThrow)
        print("Rock crushes Scissors")
        print(loser)
#IF PAPER
elif user_choice == "paper":
    if computer_choice == "rock":
        print(whatThrow)
        print("Paper covers Rock")
        print(winner)
    elif computer_choice == "scissors":
        print(whatThrow)
        print("Scissors cuts Paper")
        print(loser)
else:
    print(f"\n You typed '{user_choice}' which isn't a valid throw")
