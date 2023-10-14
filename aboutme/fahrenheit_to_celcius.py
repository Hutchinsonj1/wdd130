"""
File: fahrenheit_to_celcius.py
Author: Jaden Hutchinson

Purpose: Convert degrees in Fahrenheit to Celsius
"""

print()
fahrenheit_temp = float(input("What is the temperature in Fahrenheit? "))
calculate_fahrenheit_temp = (fahrenheit_temp - 32) * 5 / 9
print(f"The temperature in Celsius is {calculate_fahrenheit_temp:.1f} degrees.")
print()