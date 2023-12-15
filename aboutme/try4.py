
print("\n Please enter the items of the shopping list (type: quit to finish):")
print()
items = []
shopping_list = []
change_item = ""
new_item = ""
count = -1

while shopping_list != "quit":
    shopping_list = input("Item: ")
    if shopping_list != "quit":
        items.append(shopping_list)
    else:
        break
print()
print("The shopping list is:")
for i in items:
    print(i)

print()
print("The shopping list with indexes is:")
for i in items:
    count += 1
    print(f"{count}. {i}")
for i in range(len(items)):
    count += 1
    print(f"{count}. {i}")


change_item = input("Which item would you like to change? ")
new_item = input("What is the new item? ")

shopping_list[i] = new_item

for i in range(len(items)):
    items = shopping_list[i]
    print(f"{count}. {i}")

# ADD More here!

books = ["star wars","Lord of the Rings", "Harry Potter","Percy Jackson"]

for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen.