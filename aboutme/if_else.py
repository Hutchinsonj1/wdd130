print("We're going to compare integers, would you like to play? Enter Y/N to continue.")
play_game = input()
play_game.title()
print()

if play_game == "N":
    print("Let's give it a try anyway ;)" "\n")
elif play_game == "Y":
    print("Great! Here we go! :)" "\n")
else:
    print()


first_num = int(input("Enter an integer: "))
second_num = int(input("Enter another integer: "))

if first_num > second_num:
    print("The first...")