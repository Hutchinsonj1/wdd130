"""
File: physics_equation.py
Author: Jaden Hutchinson and group

Purpose: Use Python in a fairly complicated physics equation
"""
import math

print()
#  v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

play_game = input("We're going to calculate the speed of a falling object, would you like to play? Enter Y/N to continue: ")
if play_game == "N":
    print("Let's give it a try anyway ;)" "\n")
elif play_game == "Y":
    print("Great! Here we go! :)" "\n")
else:
    print()

#  v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
import math

mass = float(input("What is the mass of your object, in kg? "))
gravity = float(input("Earths or Jupiter's gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter)? "))
time = float(input("How much time, in seconds? "))
density = float(input("What is the density of the fluid (in kg/m^3, 1.3 for air, 1000 for water)? "))
cross_sectional_area = float(input("What is the cross sectional area? (in m^2)? "))
drag_constant = float(input("What is the drag constant? (0.5 for sphere, 1.1 for cylinder)? "))
print()

# Formulas commented out:
# inner_c = 1/2 * p * A * C
inner_c = float((1/2) * density * cross_sectional_area * drag_constant)

#  v(t) = sqrt(mg/c)  *  (1 - exp((-sqrt(mgc)/m)t))
velocity = float(math.sqrt(mass * gravity / inner_c) * (1 - math.exp((-math.sqrt(mass * gravity * inner_c) / mass) * time)))
print(f"The inner value of C is: {inner_c:.3f}")
print(f"The velocity after {time} seconds is {velocity:.3f} m/s")



"""
"""