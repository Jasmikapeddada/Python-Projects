from random import randint

def random():
    while True:
        n=str(randint(100,999))
        if not(n[0]==n[1] or n[1]==n[2] or n[0]==n[2]):
            return n

name=input("Welcome to the 'cows and bulls' game\nPlease enter your name:")
print("Hi ",name,", Let's Start the 'Cows and Bulls' Game",sep="")
chances=5
print("There are totally 5 possible chances to guess the number:")
ran_number=str(random())
def cows_and_bulls(ran_number,chances,cows,bulls):
    while chances>0:
        cows,bulls=0,0
        guess_number=input("Guess the number(3-digit and non repeated):")
        for i in  range(0,3):
            if ran_number[i]==guess_number[i]:
                bulls=bulls+1
            for j in range(0,3):
                if i!=j:
                    if ran_number[i]==guess_number[j]:
                        cows=cows+1
        if bulls==3:
            print("Congratulations, Your guess number is correct\nYou Won the Game")
            choice=input("Do you want to play the game again. If yes enter yes otherwise enter no:")
            if choice=='yes':
                ran_number=str(random())
                print("Welcome ",name,", lets start the game again",sep="")
                cows_and_bulls(ran_number,5,0,0)
            else:
                print("Thank you for playing the Cows and Bulls Game. Bye..")
            break
        else:
            print("there are",cows,"numbers are matched to your guess number.\nAnd there are",bulls,"places are mathced to your guess number. So, by considering this matched numbers and places enter your next guess number")
            chances=chances-1
            print("There are only",chances,"chances are left")
    if chances==0:
        print("You're out of your chances. The original number is",ran_number,".\nBest of luck next time.")
        choice1=input("Do you want to play the game again. If yes enter yes otherwise enter no:")
        if choice1=='yes':
            ran_number=str(random())
            print("Welcome ",name,", lets start the game again",sep="")
            cows_and_bulls(ran_number,5,0,0)
        else:
            print("Thank you for playing the Cows and Bulls Game. Bye..")

cows_and_bulls(ran_number,5,0,0)