"""
File: multiple_lists.py
Authors: Freddy, Nancy, Madelyn, Jaden

Purpose: Practicing Python
"""
# Create two lists to store bank accounts and balances
account_names = []
account_balances = []
account_name = ""
account_balance = ""
print("\nEnter the names and balances of bank accounts (type: quit when you done)")
# Ask for the name and balance of each bank account
while True:
    account_name = input("What is the name of this account? ")
    if account_name.lower() == "quit":
        break
    account_balance = float(input("What is the balance? "))
    account_names.append(account_name)
    account_balances.append(account_balance)
# Display the account information
print("\nAccount Information:")
for i in range(len(account_names)):  #iterating through the Number of names
    print(f"{account_names[i]} - ${account_balances[i]:.2f}")  # just adding 2 decimal 
    
# Calculate and display total balance and average balance
total_balance = sum(account_balances)
average_balance =   total_balance / len(account_names) if len(account_names) > 0 else 0
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")


# list_books = ["Harry Potter","Lord of the Rings","Chronicals of Narnia"]

# for k in range(len(list_books)):
#     book = list_books[k]
#     print(f"{k}. {book}")

