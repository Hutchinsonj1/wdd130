"""
File: fahrenheit_to_celcius.py
Author: Jaden Hutchinson

Purpose: Convert degrees in Fahrenheit to Celsius
"""

print()
fahrenheit_temp = float(input("What is the temperature in Fahrenheit? "))
calculate_celcius_temp = (fahrenheit_temp - 32) * 5 / 9
calculate_farenheit_temp = 35 * (9/5) +32
print(f"The temperature in Celsius is {calculate_farenheit_temp:.1f} degrees.")
print()
print()
celcius_temp = float(input("What is the temperature in celcius? "))
calculate_farenheit_temp = celcius_temp * (9/5) + 32
print(f"The temperature in farenheit is {calculate_farenheit_temp:.1f} degrees.")
print()