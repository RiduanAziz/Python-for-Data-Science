import random

jackpot = random.randint(1,100)

guess_number = int(input("Enter your guess number: "))

counter = 1

while guess_number != jackpot:
    if guess_number < jackpot:
        print("Wrong! Please guess higher number")

    else:
        print("Wrong! Please guess lower number")

    guess_number = int(input("Enter your guess number: "))
    counter += 1

else:
    print("You Won! Correct Guess!")
    print("Your attempt is: ",counter)

