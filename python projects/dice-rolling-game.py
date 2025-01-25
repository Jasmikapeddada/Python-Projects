# 1.Dice Rolling Game

import random

print("\nWelcome to Dice Rolling Game\n")

while True:
    choice = input("Roll the dice's (y/n): ").lower()

    if choice == "y":
        try:
            n = int(input("How many die's you want to roll at the same time: "))
            for i in range(0,n):
                die = random.randint(1,6)
                print(f"die-{i+1} value: {die}")
        except Exception:
            print("Invalid no of die's")
    elif choice == "n":
        print("Thanks for playing! ")
        break
    else:
        print("Invalid choice! ")