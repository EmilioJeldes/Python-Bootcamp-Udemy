from random import choice

print("Rock...")
print("Paper...")
print("Scissors")
player1 = input("Player 1 plays: ")

options = ["rock", "paper", "scissors"]
player2 = choice(options)

print("Computer plays " + player2)

if player1 == player2:
    print("It's a tie")
elif player1 == "rock":
    if player2 == "paper":
        print("Computer wins")
    elif player2 == "scissors":
        print("Player 1 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Computer wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("Computer wins")
    elif player2 == "paper":
        print("Player 1 wins")
else:
    print("Something went wrong")
