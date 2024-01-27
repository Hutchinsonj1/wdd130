"""
File: junk_food_counter.py
Author: Jaden Hutchinson

Purpose: Practice using Python!
"""
# Welcome
print("\nWelcome to the Junk Food Counter! Do you know what junk food you eat the most often are? ")
# Measuring sugar, times you ate it, money spent on it?
count = 0
total = 0
soda_total = []
candy_total = []
soda = input("Did you have any soda today (Enter Y/N)? ").upper()
if soda == "Y":
        daily_soda = float(input("How many did you have? "))
candy = input("Did you have any candy bars today (Enter Y/N)? ").upper()
if candy == "Y":
    daily_candy = float(input("How many candy bars did you have? "))
    # candy_total.append(daily_candy)

# print(soda_total)
# print(candy_total)

week_soda_calc = daily_soda * 7
week_candy_calc = daily_candy * 7

# print(f"If you were to continue this rate of eating candy for 1 week, you will have eaten {week_candy_calc} candy bars and drank{week_soda_calc} sodas.")

candy_fat = week_candy_calc * 12.5
candy_sugar = week_candy_calc * 40

soda_sugar = week_soda_calc * 2222

"""
How much Sugar in:
Conclusion: "Average 20oz soda contains 65 grams". If we use this same calculation for a 12oz can of soda, each would contain an average of 39 grams of sugar.

Standard soda:
Coke: 40
Pepsi: 41
Sprite: 26
Bundaberg Ginger Beer: 41
Mountain Dew: 46
Dr Pepper: 40
Cream Soda: 66
7up: 38
Orange Soda: 43
Minute Maid Lemonade: 40
Mountain Dew: 46

# Mountain Dew (20oz): 77
"""
# Average Energy drink: 45 grams
# Red Bull: 37
# Monster: 54
# Gatorade: 38
# Rockstar: 63

sugar_total = 3
fat_total = 5

print(f"Based on the average amount of sugar and Fat in: a candy bar, soda, and energy drink, you will have consumed {sugar_total} grams of sugar and {fat_total} grams of fat in just one week.")

print("Here are some links to help you conquer these bad habits: atomichabits.com,")

print(f"The average candy bar contains 12.5 grams of fat and 40 grams of sugar, the average energy drink contains _ grams and the average soda contains _ grams of sugar, respectively. Based on these, you will have consumed {candy_fat} grams of fat and {candy_sugar} grams of sugar from candy, and {soda_sugar} grams of sugar in one week.")