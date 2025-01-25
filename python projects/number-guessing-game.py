# 2.Number Guessing Game

import random

num = random.randint(1,100)
#print(num)

while True:
    try:
        guess = int(input("\nGuess the number between 1 and 100: "))

        if guess > 100:
            print("Your guess number is bigger than 100!")
        elif guess < 1:
            print("Your guess number is smaller than 1!")
        else:
            if guess == num:
                print("Congratulations! Your guess number is correct")
                break
            elif guess > num:
                print("Too high!")
            elif guess < num:
                print("Too low!")
    except ValueError:
        print("Please enter valid number")