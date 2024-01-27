"""
File: fast_food_expend.py
Author: Jaden Hutchinson

Purpose: Practice using Python to create a Monthly Fast Food Expendature Application
"""
# Welcome
print("\nWelcome to the Monthly Fast Food Expendature Application! For the best accuracy, please have receipts ready or make your best guess for each week. ")
count = 0
total = 0
# Setting max weeks to 4 with a count
while count < 5:
    count = int(input("\nWhat week of the month is it (1-4)? "))
    times_per_week = float(input("How many times did you go out to fast food this week? "))
    amount_per_time = float(input("Approximately how much did you spend each time you went out? "))
    week_total = times_per_week * amount_per_time 
    count += 1
    total = total + week_total

print(f"\nYour Monthly Fast Food Expendature is: ${total:.2f}") 

# Average 
average = total / 4
print(f"\n\nYour average weekly expedature is: ${average:.2f}\n") # :.2f to round to 2 decimal places, as needed
# Thanks for playing
print("Thanks for playing!\n")




