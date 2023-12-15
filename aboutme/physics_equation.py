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

"""
m = mass (in kg)

g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)

t = time (in seconds)

c = 1/2 p A C

p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)

A = cross sectional area of projectile (in square meters)

C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)

exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

Hints: You can find the cross sectional area of a bowling ball by using its radius and calculating the area (pi*r^2). You can approximate the drag constant for a loaf of bread by thinking about it as a cylinder. Do your best to estimate the cross sectional area of a skydiver. Are they falling head first or lying flat? You can look up values for the drag constant of a skydiver.
"""
import math

mass = float(input("What is the mass of your object, in kg? "))
gravity = float(input("Earths or Jupiter's gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter)? "))
time = float(input("How much time in seconds? "))
p = float(input("What is the density of the fluid (in kg/m^3, 1.3 for air, 1000 for water)? ")) #Density
a = float(input("What is the cross sectional area? (in m^2)? ")) #drag constant
c = float(input("What is the drag constant? (0.5 for sphere, 1.1 for cylinder)? "))
bowling_ball = input("Is this a bowling ball (Y/N)? ").lower()
if bowling_ball == "y":
    radius_bowling_ball = float(input("What is it's radius? "))
    cross_sect_bowling_ball = float((math.pi) * pow(radius_bowling_ball, 2))
    a = cross_sect_bowling_ball
bread = input("Is this a loaf of bread? ").lower()


print()

# Formulas commented out: inner_c = 1/2 * p * A * C
inner_c = float((1/2) * p * a * c)

#  v(t) = sqrt(mg/c)  *  (1 - exp((-sqrt(mgc)/m)t))

#exp means EXPONENT *the following*
#sqrt means SQUARE ROOT *the following*
velocity = 0
velocity = math.sqrt(mass*gravity/inner_c) * (1 - math.exp((-math.sqrt(mass * gravity * inner_c)/mass) * time))
print(f"The inner value of C is: {inner_c:.3f}")
print(f"The velocity after {time} seconds is {velocity:.3f} m/s")


"""
Try determining the velocity for a few different objects that you know. For example, you might try a bowling ball, a loaf of bread, and a skydiver.

Hints: You can find the cross sectional area of a bowling ball by using its radius and calculating the area (pi*r^2). You can approximate the drag constant for a loaf of bread by thinking about it as a cylinder. Do your best to estimate the cross sectional area of a skydiver. Are they falling head first or lying flat? You can look up values for the drag constant of a skydiver.
"""