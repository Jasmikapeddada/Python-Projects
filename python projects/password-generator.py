import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '?', '<', '>']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("\nWelcome to the Password Generator!\n")
no_letters = int(input("How many letters would you like in your password? "))
no_symbols = int(input("How many Symbols would you like? "))
no_numbers = int(input("How many numbers would you like? "))
password_list = []

for i in range(no_letters):
    letter = random.choice(letters)
    password_list += letter

for i in range(no_symbols):
    symbol = random.choice(symbols)
    password_list += symbol

for i in range(no_numbers):
    number = random.choice(numbers)
    password_list += number

random.shuffle(password_list)

password  = ""

for i in password_list:
    password += i

print("\nPassword: ",password, "\n")