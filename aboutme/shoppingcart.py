"""
File: shoppingcart.py
Author: Jaden Hutchinson

Purpose: Practice using Python to make a item adding/subtracting shopping cart with Total price

"""
print("\nWelcome to the Shopping Cart Program!")

action = None
items = []
new_item = []
price = []
prices = []
remove = []
total_p = 0
item_count = 0

while action != "quit":
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")

    if action == "1":
            # Append items, if not "done"
            new_item = input("What item would you like to add? ")
            items.append(new_item)
            price = float(input("What is the price of '{}'? ".format(new_item)))
            prices.append(price)
            print(f"'{new_item}' has been added to cart.")

    elif action == "2":
        print("The contents of the shopping cart are: ")

        for i in range(len(items)):
             item = items[i]
             price = prices[i]
             item_count += 1
             print(f"{item_count}. {item} - ${price:.2f}")
        
    elif action == "3":
        remove = int(input("What item would you like to remove? "))
        items.pop(remove)
        print("Item removed.")

    elif action == "4":
        for i in range(len(items)):
            total_p += prices[i]
        print(f"The total price of the items in the shopping cart is: {total_p}")

    elif action == "5":
        action == "quit"
        print("Thank you. Goodbye. If you want to try again, just restart the program!")
        break

    else:
        print("Please enter a valid choice.")