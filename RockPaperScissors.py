import random

while True:
    choices = ["rock","paper","scissors"]
    
    P2 = random.choice(choices)
    P1 = None

    while P1 not in choices:
        P1 = input("Player 1: ").lower()

    if P1 == P2:
        print("Player 2: ",P2)
        print("Tie!")

    elif P1 == "rock":
        if P2 == "paper":
            print("Player 2: ", P2)
            print("You lose!")
        if P2 == "scissors":
            print("Player 2: ", P2)
            print("You win!")

    elif P1 == "scissors":
        if P2 == "rock":
            print("Player 2: ", P2)
            print("You lose!")
        if P2 == "paper":
            print("Player 2: ", P2)
            print("You win!")

    elif P1 == "paper":
        if P2 == "scissors":
            print("Player 2: ", P2)
            print("You lose!")
        if P2 == "rock":
            print("Player 2: ", P2)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
