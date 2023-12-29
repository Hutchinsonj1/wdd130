"""
File: try4.py
Authors: Freddy, Brook Ann, Nancy, Madelyn, Jaden

Purpose: Practice using Python to find the Sum, Average, and Max numbers of a list manually

Sum = ADD all numbers
Average = ADD all numbers, then just divide!
Max = still iterate (loop) through all numbers, but identify the MAX number
"""
print("Enter a list of numbers, type 0 when finished.")
print()
# Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
new_number = ""
numbers = []
total = -1
# Average is total nubmers, Divided by the total NUMBER of numbers
while new_number != 0:
    new_number = int(input("Enter a number: "))

    if new_number != 0:
        numbers.append(new_number)
        total = total + new_number
    # if new_number > 0:
    #     pos_number_list.ap7


print(f"\nThe sum is: {total:.2f}")

#Average
count = len(numbers)  
average = total / count
print(f"The average is: {average}")

# There is a function we found called 'max', and it works great
x = max(numbers)
y = min(numbers)
print(f"The largest number is: {x}")
print(f"The smallest number is: {y}")
print()



