"""
File: madlibs_game.py
Author: Jaden Hutchinson

This program is a Mad Libs Word Game!

Purpose: To practice formatting strings.
"""

print("We're going to create a Mad Libs story, would you like to participate? Enter Y/N to continue.")
play_game = input();
play_game.title()
print()

if play_game == "N":
    print("Let's give it a try anyway ;)" "\n")
elif play_game == "Y":
    print("Great! Here we go! :)" "\n")
else:
    print()

print("Enter an adjective:")
adjective = input();

print("Enter the name of an animal:")
animal_name = input();

print("Enter a verb:")
verb = input();

print("Enter an exclamation:")
exclamation = input();

print("Enter another verb:")
verb2 = input();

print("Enter just one more verb!")
verb3 = input();

print("\n")
print("Please enter the following:" "\n")

print("adjective: "+"\033[4m"+ adjective + "\033[0m")
print("animal: "+"\033[4m"+ animal_name + "\033[0m")
print("verb: "+"\033[4m"+ verb + "\033[0m")
print("exclamation: "+"\033[4m"+ exclamation + "\033[0m")
print("verb: "+"\033[4m"+ verb2 + "\033[0m")
print("verb: "+"\033[4m"+ verb3 + "\033[0m" +"\n")

print("Your story is: \n")

print(f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal_name} {verb} down the hallway.'{exclamation.title()}'! I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family." "\n")

print("Thanks for playing!")




