"""
File:
Author: Jaden Hutchinson

Purpose: Practice using Python

Start by asking the user for the magic number. (In future steps, we will change this to have the computer generate a random number, but to get started, we'll just let the user decide what it is.)

Ask the user for a guess.

Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it.

At this point, you won't have any loops.
"""

#step 01: Only one time through, so an IF statement FOR NOW works: 
# magic_number = int(input("What is the magic number? "))
# guess_number = int(input("What is your guess? "))
# if guess_number < magic_number:
#     print("Higher")
# elif guess_number > magic_number:
#     print("Lower")
# else:
#     print("You guessed it!")

# #Now for... step 02! (Adding a LOOP)
# magic_number = 0
# guess_number = 1
# while guess_number != magic_number:
#     magic_number = int(input("What is the magic number? "))
#     guess_number = int(input("What is your guess? "))
#     if guess_number < magic_number:
#         print("Higher")
#     if guess_number > magic_number:
#         print("Lower")

# print("You guessed it!")


import random

print("\nCan you guess the magic number?")

magic_number = random.randint(0,10)
guess_number = 0
while guess_number != magic_number:
    guess_number = int(input("What is your guess? "))
    if guess_number < magic_number:
        print("Higher")
    if guess_number > magic_number:
        print("Lower")

print("You guessed it!\n")
