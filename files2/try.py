# # """
# # File: try.py
# # Author: Jaden Hutchinson

# # Purpose: Practice Python in parsing and splitting strings
# # """
# # colors = "red blue green yellow"

# # color_parts = colors.split()

# # print(colors)
# # print(color_parts)

# # second = color_parts[1]

# # print(second)

# # clients = []
# # new_client = ""

# # # I like the creativity, but "solving puzzles" might not always be my favorite
# # while new_client != "quit":
# #     new_client = input("What is the name of the client? ")
# #     if new_client != "quit":
# #         clients.append(new_client)

# # for client in clients:
# #     print(client)
# # salary = []
# tips = []
# salary = float(input("What is your salary? "))
# print(salary)
# while tips != "done":
#     salary = salary + 1
#     tips = float(input("What is your tip today? "))
#     if tips != "done":
#         salary.append(tips)
# salary = [90]
# tips = [8.95, 12.50, 11.20]
# salary.append(tips)

# print(salary) # puts two lists together... [90, [8.95, 12.5, 11.2]]
# # print(sum(tips))

clients = []

new_client = ""
while new_client != "quit":
    new_client = input("What is the name of the client? ")
    if new_client != "quit":
        clients.append(new_client)
        # clients.append("John")
print()
for client in clients:
    print(client)
# print(clients)