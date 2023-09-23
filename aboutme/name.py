# print("What is your first name?")
# f_name = input();
# print("What is your last name?")
# l_name = input();

# print("Your name is %s," % l_name, f_name , "%s." % l_name)

# # OR:
# # print(f"Your name is {l_name}, {f_name} {l_name}.")
print("We're going to create a Mad Libs story, would you like to participate? Enter Y/N.")

# for x in pg:
#   pg = input()
# if pg == "N":
#   print("Ok. Thank you, come again!")
# elif pg == "Y":
#   continue
# else:
#   print("a is greater than b")
while True:
    a = input("Enter yes/no to continue")
    if a=="yes":
        # gameplay()
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no")