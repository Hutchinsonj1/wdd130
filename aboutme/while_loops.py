"""
File: while_loops.py
Author:

Purpose: To practice Python

Please type a positive number: -3
Sorry, that is a negative number. Please try again.
"""

number = int(input("Please enter a positive number: "))


#WHILE THIS IS TRUE:
while number <= -1:
    print("The number cannot be negative.")
    number = int(input("Please enter a positive number: "))
    # Jump BACK up to line 15

print("Finished with the loop\n")

 
# candy = "no"

# while candy != "yes":
#     candy = input("May I have a piece of candy? ")

# print("Thank you")
