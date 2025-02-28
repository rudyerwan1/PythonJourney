"""
#loops for range etc

for number in range (1,101):
    number = number + 100
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    #elif number % 3 and number % 5 == 0:
#       print("FizzBuzz")

    else :
        print(number)

"""
#from typing import final

"""
#Password generator,
import random
letters = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h','i','j','k','l', 'm']
numbers =['0','1','2','3','4', '5', '6' '7','8','9']
symbols = ['!', '#', '$','%','&', '(',')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!)")
mr_letters = int(input("How many letters would you like in your password?\n"))
for i in range (mr_letters):
    password.append(random.choice(letters))
mr_symbols = int(input(f"How many sysmbols would you like ?\n"))
for i in range (mr_symbols):
    password.append(random.choice(symbols))
mr_numbers = int(input(f"How many number would you lie?\n"))
for i in range (mr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
final_password = ''.join(password)
print(f" Here is your new password {final_password}")"""

#Exercie Build a Secret Phrase Generator

"""Secret Phrase Generator
The objective is to create a program that generates a secret phrase composed of random words,
numbers, and symbols to create a memorable but secure passphrase.
Required Features:

The program should ask the user:

How many words they want in their phrase
If they want to include numbers between words (yes/no)
If they want to include symbols between words (yes/no)


The program should:

Choose random words from a predefined list
Add random numbers between words if requested
Add random symbols between words if requested
Display the final secret phrase"""

import random

# Lists of elements
words = ['dog', 'cat', 'house', 'tree', 'car', 'book', 'sun', 'moon',
         'table', 'chair', 'door', 'window', 'mountain', 'river', 'ocean']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '?', '+', '-']
secret_phase = []

# Complete the program!
# Ask how many words the user wants
nb_words = int(input("How Many word would you like ?\n"))
add_numbers = input("Would you like numbers in your code select yes/no ?\n").lower() == "yes"
add_symbols = input("Would you like symbols in your code ?\n").lower() == "yes"
for i in range (nb_words):
    secret_phase.append(random.choice(words))
    if i < nb_words -1 :
        if add_numbers:
            secret_phase.append(random.choice(numbers))
        if add_symbols:
            secret_phase.append(random.choice(symbols))
    else:
        print("ok sounds good no number or symbols")
final_secret_phrase = ''.join(secret_phase)
print(f"here you secret phrase buddy ! {final_secret_phrase}")