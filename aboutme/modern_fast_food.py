"""
File: modern_fast_food.py
Author: Jaden Hutchinson

Purpose: Practice using Python to create a Monthly Fast Food Expendature application
"""
print("\nWelcome to the Monthly Fast Food Expendature Application! For the best accuracy, please have receipts ready or make your best guess for each week. ")
count = 0

while count < 5:
    count = int(input("\nWhat week is it (1-4)? "))
    count += 1

# wk1_reminder = "Remember to enter how much you spent this week in fast food into your fast food app at 7pm tonight.\n"
    # for i in range(4):
    weeks = float(input("How many times did you go out to fast food this week? "))
    week1_amt = float(input("Approximately how much did you spend each time you went out? "))

# Setting variables to enter the loop
new_number = ""
numbers = []
total = -1
# Average is total nubmers, Divided by the total NUMBER of numbers
while new_number != 0: # Just a Way to enter/exit the loop (0)
    new_number = int(input("Enter a number: "))

    if new_number != 0:
        numbers.append(new_number)
        total = total + new_number


print(f"\nThe sum is: {total:.2f}")

#Average
count = len(numbers)  
average = total / count
print(f"The average is: {average}")
 





