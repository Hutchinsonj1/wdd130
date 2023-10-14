"""
File: grade_calculator2.py
Authors: Madelyn, Brook Ann, Freddy, Jaden

Purpose: Use Python to solve problems, including creating a grade calculator.

A >= 90

B >= 80

C >= 70

D >= 60

F < 60

Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.
"""
grade_calculator = int(input("What is your grade percentage? "))

if grade_calculator >= 90:
    if grade_calculator >= 94:
        letter = "A"
    else:
        letter = "-A"
elif grade_calculator >= 80:  #ELIF is anytime previous Statements were NOT true :)
    if grade_calculator >= 87:
        letter = "+B"
    elif grade_calculator <= 86 and grade_calculator >= 84:
        letter = "B"
    else:
        letter = "-B"
elif grade_calculator >= 70:
    if grade_calculator >= 77:
        letter = "+C"
    elif grade_calculator <= 76 and grade_calculator >= 74:
        letter = "C"
    else:
        letter = "-C"
elif grade_calculator >= 60:  #ELIF is anytime previous Statements were NOT true :)
    if grade_calculator >= 67:
        letter = "+D"
    elif grade_calculator <= 66 and grade_calculator >= 64:
        letter = "D"
    else:
        letter = "-D"
else: #NOTHING else before this was true
    letter = "F"


# Trying another way: Divide by 10, except you have to redo A and F...
# grade_percentage = grade_percentage % 10

print(f"Your letter grade is {letter}")


"""
Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.
"""
if grade_calculator >= 70:
    print("Congratulations! You passed the class.")
else:
    print("Sorry, you didn't pass the class. Try harder next time!")


print("\n""Thanks for playing! Have a good day!""\n")

