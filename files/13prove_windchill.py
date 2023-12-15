"""
File: 13prove_windchill.py
Author: Jaden Hutchinson

Purpose: Practice using Python to calculate windchill
"""
# Wind-chill function:
# wind-chill = 35.74 + (0.6215 * temp)  - (35.75 * (speed ** 0.16))  + (0.4275 * temp * (speed ** 0.16))

temp = 0
speed = 0
print()
# while speed != "quit":
def wind_chill(temp, speed=0):
        wind_chill_calc = 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))
        return wind_chill_calc

temp = float(input("What is the temperature? "))
# OPTIONAL: If asking for wind-speed rather than displaying by 5's below.
# speed = float(input("What is the wind speed? "))
celcius_or_farenheit = input("Farenheit or Celcius (F/C)? ").upper()

if celcius_or_farenheit == "C":
        temp = temp * (9/5) + 32

# Original function call:
# wind_chill_function = wind_chill(temp,speed)
wind_chill_5 = wind_chill(temp,speed=5)
wind_chill_10 = wind_chill(temp,speed=10)
wind_chill_15 = wind_chill(temp,speed=15)
wind_chill_20 = wind_chill(temp,speed=20)
wind_chill_25 = wind_chill(temp,speed=25)
wind_chill_30 = wind_chill(temp,speed=30)
wind_chill_35 = wind_chill(temp,speed=35)
wind_chill_40 = wind_chill(temp,speed=40)
wind_chill_45 = wind_chill(temp,speed=45)
wind_chill_50 = wind_chill(temp,speed=50)
wind_chill_55 = wind_chill(temp,speed=55)
wind_chill_60 = wind_chill(temp,speed=60)
# print(wind_chill_function)
print(f"At temperature {temp}F, and wind speed 5 mph, the windchill is: {wind_chill_5:.2f}F")
print(f"At temperature {temp}F, and wind speed 10 mph, the windchill is: {wind_chill_10:.2f}F")
print(f"At temperature {temp}F, and wind speed 15 mph, the windchill is: {wind_chill_15:.2f}F")
print(f"At temperature {temp}F, and wind speed 20 mph, the windchill is: {wind_chill_20:.2f}F")
print(f"At temperature {temp}F, and wind speed 25 mph, the windchill is: {wind_chill_25:.2f}F")
print(f"At temperature {temp}F, and wind speed 30 mph, the windchill is: {wind_chill_30:.2f}F")
print(f"At temperature {temp}F, and wind speed 35 mph, the windchill is: {wind_chill_35:.2f}F")
print(f"At temperature {temp}F, and wind speed 40 mph, the windchill is: {wind_chill_40:.2f}F")
print(f"At temperature {temp}F, and wind speed 45 mph, the windchill is: {wind_chill_45:.2f}F")
print(f"At temperature {temp}F, and wind speed 50 mph, the windchill is: {wind_chill_50:.2f}F")
print(f"At temperature {temp}F, and wind speed 55 mph, the windchill is: {wind_chill_55:.2f}F")
print(f"At temperature {temp}F, and wind speed 60 mph, the windchill is: {wind_chill_60:.2f}F")
print()
print("Thanks for playing!\n")

