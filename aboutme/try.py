# # # # # var1 = int(input("Enter a number: "))

# # # # # print(type(var1))

# # # # while True:
# # # #     a = int(input("> "))
# # # #     if a == 1:
# # # #         print("this")
# # # #         break
# # # #     print("You have made an invalid choice, try again.")


# # # # while value < 20:
# # # #    value = value + 1
# # # # print(value)

# # # # items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

# # # # for item in items:
# # # #     print(item)

# # # # colors = ["red","blue","green","yellow"]

# # # # for color in colors:
# # # #     print(color)
# # # # print()

# # # # for i in range(100, 200):
# # # #     print(i)

# # # # for i in range(1,9):
# # # #     print(i)
# # # # print()

# # # # This loop will do the same thing, but this time, it will count by 10's
# # # # for i in range(100, 200, 10):
# # # #     print(i)

# # # # for j in range(2,22,2):
# # # #     print(j)

# # # # print("Welcome to the word guesing game!""\n")
# # # # word = input("What is your guess?")
# # # # number_of_letters = len(word)

# # # # for i in range(number_of_letters):
# # # #     letter = word[i]
# # # #     print(f"Index: {i} Letter: {letter}")

print()
clients = []  # ALL
new_client = []  #One at a time entered by user

while new_client != "quit":
    new_client = input("What is the name of the client? ")
    if new_client != "quit":
        clients.append(new_client)

for client in clients:
    print(client)






# # # total, average, largest...
# new_amount = []
# running_total = 0
# run_program = False

# new_amount = float(input("What is the balance? "))
# while(not run_program):
#     if run_program != True:
#         running_total += new_amount
#     print(f"The running total is {running_total:.2f}")

# # age = 30
# # age = age + 1
# # print(age)

# # receipts =  [70,20,10,12.50]

# # running_total = 0
# # for receipts in receipts:
# #     running_total += receipts

# # print(f"Your running total is {running_total}")
