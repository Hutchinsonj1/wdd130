"""
File: grade_calculator.py
Author: Jaden Hutchinson

Purpose: Use Python to solve problems, including creating a grade calculator
"""

grade_percentage = int(input("What is your grade percentage? "))
print()
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your letter grade is {letter}")

if grade_percentage >= 60:
    print("You passed the course!")
else:
    print("Sorry, you did not pass the course.")

"""
A >= 90

B >= 80

C >= 70

D >= 60

F < 60


Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.


Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.
"""