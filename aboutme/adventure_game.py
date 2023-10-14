"""
File: adventure_game.py
Author: Jaden Hutchinson

Purpose: Practicing Python more!
"""
# You are walking through a dark forest and find two items: 

scenario_1 = input(f"You are walking through a misty jungle at night, and you hear branches suddenly crack to your left. What do you do: RUN or HIDE ").lower()
if scenario_1 == "run":
    first_you_run = input("You decide to sprint ahead, hoping whatever made that loud cracking sound won't be able to catch you.Once you run what you feel is far enough you slow down to catch your breath. Just to be safe, you slowly turn your head around to see a large dark mass pouncing towards you at full speed. Do you CLIMB A TREE or KEEP RUNNING? ").lower()
    if first_you_run == "climb a tree":
        second_you_climb = input("You've decided to scramble up the closest tree to you as fast as you can. You can hear him below but you just keep climbing. You find the skeleton of a previous climber and you get worried. You find on him two things that could help you survive. Do you want the BANDANA or a NERF GUN? ")
        third_you_bandana = input("Good choice. Since the beast probably can't see you if you can't see him you decide to blindful yourself. You can now jump down from the tree or ")

""" 
You need to have at least three levels of scenarios with possible choices.
At least one of your scenarios must have more than two possible choices.
"""
