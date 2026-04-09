#ROCK PAPER SCISSOR GAME

import random
options = ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Pick your choice(rock,paper,scissors):")

    print(f"Your choice : {player}")
    print(f"Computer's choice : {computer}")

    if player == computer:
        print("It's a tie..")
    elif player == "rock" and computer =="scissors":
        print("You won....")
    elif player == "scissors" and computer == "paper":
        print("You won....")
    elif player == "paper" and computer == "rock":
        print("You won....")
    else:
        print("Oops...You lost...Try again...")

    play_again = input("Want to play again??(y/n):").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing our rock,paper,scissors...")

