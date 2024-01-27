age = input("\nHow old are you? ")
print("On your next birthday, you will be", int(age) + 1)

egg_cartons = input("\nHow many egg cartons do you have? ")
print("You have", int(egg_cartons) * 12,"eggs\n")

cookies = input("How many cookies do you have? ")
people_num = input("How many people are there? ")
print("Each person can have ", float(cookies) // float(people_num),"cookies","or ", float(cookies) / float(people_num),"whole cookies.")
# print(people_num:.2f)