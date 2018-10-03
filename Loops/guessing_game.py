from random import randint

random_number = randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess > random_number:
        print("Too High!!")
    elif guess < random_number:
        print("Too low")
    else:
        print("You Won!!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            random_number = randint(1, 10)
            guess = None
        else:
            print("Thank you for playing")
            break
