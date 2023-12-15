"""
File: amusementpark2.py
Authors: Jaden Hutchinson

Purpose: Practice Python while making an Amusement Park game
"""
#Boolean variable, set to False by default
can_ride = False

age_f_rider = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))

if_second_rider = input("Is there a second rider (yes/no)? ").lower()

if if_second_rider == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))

    # Rule 1
    if height1 < 36 or height2 < 36: # Assuring BOTH are at least 36 inches tall
        can_ride = False
    else:
        # Rule 3
        if age_f_rider >= 18 or age2 >= 18:
            # At least one is an adult
            can_ride = True
        else:
            # Neither is an adult
            can_ride = False
elif if_second_rider != "yes" and if_second_rider != "no":
    print("\n""Please restart the program and type either yes/no to the last question.")

else: # There is only one rider
    # Rule 2
    if age_f_rider >= 18 and height1 >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")