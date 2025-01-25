# 3.Rock Paper Scissor

import random

print("\nWelcome to Rock Paper Scissor Game\n")

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
options = tuple(emojis.keys())
your_points = 0
comp_points = 0

def get_comp(chances):
    comp = random.choice(options)
    print(f"\nYou have {chances} chances")
    choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
    return comp, choice

def valid_choice(comp, choice, your_points, comp_points, chances):
    if choice == comp:
        chances -= 1
        print(f"You chose {emojis[choice]}\nComputer chose {emojis[comp]}\nDraw")
        print(f"Your points: {your_points}, Computer points: {comp_points}")
    elif (choice == 'r' and comp == 'p') or (choice == 'p' and comp == 's') or (choice == 's' and comp == 'r'):
        print(f"You chose {emojis[choice]}\nComputer chose {emojis[comp]}\nYou lose")
        comp_points += 1
        chances -= 1
        print(f"Your points: {your_points}, Computer points: {comp_points}")
    else:
        print(f"You chose {emojis[choice]}\nComputer chose {emojis[comp]}\nYou win")
        your_points += 1
        chances -= 1
        print(f"Your points: {your_points}, Computer points: {comp_points}")
    return chances, your_points, comp_points

def determine_output(your_points, comp_points):
    if your_points > comp_points: print(f"\nFinally, You won the game with {your_points} points\n")
    elif your_points < comp_points: print(f"\nFinally, Computer won the game with {comp_points} points\n")
    else:
        print(f"\nFinnaly Draw, You and Computer won the match with {your_points} points\n")

def try_case(your_points, comp_points):
    chances = int(input("In how many chances do you want to play the game with computer? "))

    if chances == 0:
        print("Invalid choice")
    else:
        while chances != 0:
            comp, choice = get_comp(chances)
        
            if choice in options:
                chances, your_points, comp_points = valid_choice(comp, choice, your_points, comp_points, chances)
            else:
                print("Invalid choice!")

        if chances == 0:
            determine_output(your_points, comp_points)

def handling_exception(your_points, comp_points):
    try:
        try_case(your_points, comp_points)

    except Exception as e:
        print("Invalid chances!", e)

handling_exception(your_points, comp_points)