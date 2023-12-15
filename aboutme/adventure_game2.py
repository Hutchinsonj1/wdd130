"""
File: adventure_game2.py
Author: Jaden Hutchinson

Purpose: Practice Python!

# Example: "You are walking through a dark forest and find two items"...

--> You need to have at least three levels of scenarios with possible choices.
--> At least one of your scenarios must have more than two possible choices.
"""
print()
# use While Loops so I can break and then continue the code whenever an invalid response is entered.
while True:
    scenario_1 = input("You are on a boat in the middle of a storm, do you want to turn the boat EAST or WEST? ").lower()
    if scenario_1 == "east":
        turning_east = input("You've decided to turn east. It's getting darker and colder. You find a MATCH and an UMBRELLA on your ship. Which do you want to use? ").lower()
        if turning_east == "match":
            match = input("You want to use your match to light a lantern. You try again and again to start the match but it won't light. Do you give up and SLEEP or search FLAMMABLE MATERIALS? ").lower()
            break
        elif turning_east == "umbrella":
            umbrella = input("You pull out the umbrella, and the storm becomes worse. You see a large whale in the front of the stern, do you turn RIGHT or LEFT? ").lower()
            break     
        else:
            print()
        print("You have made an invalid choice, try again.")
        
    elif scenario_1 == "west":
        turning_west = input("You've decided to turn west. Things are lightening up a little. Oboard you find a FISHING POLE, a COMPASS and a LANTERN. Which do you choose? ").lower()
        if turning_west == "fishing pole":
            fishing_pole = input("You figure since the weather is lightening up a bit you might as well try you hands at fishing instead of just steering the boat. You throw the line in the water, and before long you get something very heavy, so heavy you're worried your line may break. Do you REEL IT IN or CUT THE LINE? ").lower()
            if fishing_pole == "reel it in":
                reel_it_in = input("You struggle reeling it in. The rod bends, then snaps. You see a large shark fin next to your boat. Do you HARASS THE SHARK, PANIC, or ROW THE BOAT (away from him)? ").lower()
                if reel_it_in == "harass the shark":
                    print("You decide to throw rocks from your boat at the shark. This does not make the shark very happy. It turns and bites a huge hole in your vessel. You are now beginning to sink. Good luck getting out alive!")  
                    break
                elif reel_it_in == "panic":
                    print("You decide to panic. This may not help your situation.")
                    break
                elif reel_it_in == "row the boat":
                    print("Nice choice. You don't want to take any chances!")
                    break
                else:
                    print("Invalid choice. Please try again")
                break

            elif fishing_pole == "cut the line":
                print("Good choice. Better luck next time!")
                break
            else:
                print("Please enter a valid choice.")
            break
    
        elif turning_west == "compass":
            compass = input("The compass can lead you wherever you like. Going North will take you further on your adventure, South will take you towards home. NORTH or SOUTH? ").lower()
            break
        elif turning_west == "lantern":
            lantern = input("You light your lantern and its' light provides some solace. Upon hitting a wave it falls to the ship floor and starts the deck on fire. Do you PUT OUT THE FIRE or JUMP OVERBOARD?").lower()
            break
        else:
            print("Please enter a valid choice.")
        break
    else: 
        print("Please enter a valid choice.")


# while True:
#     a = int(input("> "))
#     if a == 1:
#         print("this")
#         break
#     if a == 2:
#         print("that")
#         break
#     print("You have made an invalid choice, try again.")


# if scenario_1 == "east":

# elif scenario_1 == "west":

# else:
    # print("Please enter a valid choice.")