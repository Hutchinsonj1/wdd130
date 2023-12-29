"""
File: try.py
Author: Jaden Hutchinson

Purpose: Practice Python in parsing and splitting strings
"""
colors = "red blue green yellow"

color_parts = colors.split()

print(colors)
print(color_parts)

second = color_parts[1]

print(second)

clients = []
new_client = ""

# I like the creativity, but "solving puzzles" might not always be my favorite
while new_client != "quit":
    new_client = input("What is the name of the client? ")
    if new_client != "quit":
        clients.append(new_client)        

for client in clients:
    print(client)





