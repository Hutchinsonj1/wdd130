"""
File: functions2.py
Authors: Nancy, Madelyn, Jaden

Purpose: Practice using functions with Python
"""

# How to calculate:
#   square: side ** 2
#   rectangle: length * width
#   circle: PI * (radius ** 2)

print()
shape = ""
while shape != "quit":
    shape = input("What shapes area do you want? ").lower()

    if shape == "square":
        def compute_area_square(side):
            square = side ** 2
            return square

        side = int(input("What is the length of one side of the square? "))
        square_function = compute_area_square(side)

        print(square_function)
        print()

    elif shape == "rectangle":
        def compute_area_rectangle(length,width):
            rectangle_area = length * width
            return rectangle_area

        length = int(input("What is the length of a rectangle? "))
        width = int(input("What is the width of a rectangle? "))

        rectangle_function = compute_area_rectangle(length,width)

        print(rectangle_function)
        print()

    elif shape == "circle":
        import math
        def compute_area_circle(radius):
            circle_area = math.pi * (radius ** 2)
            return circle_area

        radius = float(input("What is radius of the circle? "))
        circle_function = compute_area_circle(radius)

        print(circle_function)
        print()

print("Thanks for playing!")


