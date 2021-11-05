

import random

number = random.randint(1,100)

while True:
    guess = int(input("Guess a integer number 1 to 100 "))
    if guess < number:
        print("Increase your number ")
    elif guess > number:
        print("Decrease your number ")
    else:
        print("Correct !!! ")
        break
    

