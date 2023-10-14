"""
File: meal_price_plan.py
Author: Jaden Hutchinson

Purpose: Practice using Python with math; specifically create a meal price plan.
"""

play_price_plan = input("We're going to calculate a meal price plan for you, would you like to participate? Enter Y/N to continue: ")
if play_price_plan == "N":
    print("Let's give it a try anyway ;)" "\n")
elif play_price_plan == "Y":
    print("Great! Here we go! :)" "\n")
else:
    print("\n")

print() #printing a blank line
child_meal = input("What is the price of a child's meal? ")
adult_meal = input("What is the price of an adult meal? ")
n_of_children = input("How many children are there? ")
n_of_adults = input("How many adults are there? ")

# Type casting, to allow for string concatenation:
child_total = float(child_meal) * int(n_of_children)
adult_total = float(adult_meal) * int(n_of_adults)

s_tax_percentage = input("What is the sales tax rate? ")
s_tax_decimal = float(s_tax_percentage) / 100
print()

subtotal = child_total + adult_total
print(f"Subtotal: ${subtotal:.2f}")

total_tax = subtotal * s_tax_decimal
print(f"Sales Tax: ${total_tax:.2f}")

final_total = total_tax + subtotal
print(f"Total: ${final_total:.2f}")
print()

amt_paid = input("What is the payment amount? ")
change = float(amt_paid) - final_total
print(f"Change: ${change:.2f}")
print("\n")



"""
General tips for my classmates:
Ask the User the question
Assign a Variable to every answer asked of the user. Have their answer displayed on the same line.
Print every answer as a float (not an integer), for the purpose of accounting. 
Make sure only people are casted to ints.

Take ALL of answers from User and Calculate *something*

float = number with a decimal
integer = whole number
"""


