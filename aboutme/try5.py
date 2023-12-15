"""
File: try5.py
Authors: Jaden Hutchinson

Purpose: Practice Python to combine/compare two different lists
"""

# 3 account names
# 3 account Balances
#
total = 0
average = ""
# account[0]
# running_total += new_amount

# ONE loop for Balances, ONE for account

# Need a loop for all 3 accounts
print("Enter the names and balances of bank accounts (type: quit when done)")

balances = []
new_account = []
accounts = [] #
while new_account != "quit":
    new_account = input("What is the name of this account? ").lower()
    
    if new_account != "quit":
        balance = float(input("What is the balance? "))

        accounts.append(new_account)
        balances.append(balance)


for i in range(len(accounts)):
    # AFTER THIS is NEW:
    print(f"{accounts}: {balances}")


print("Account Information:")
print(f"checking: ${check_bal}")
print(f"savings: ${savings_bal}")
print(f"emergency fund: ${emergency_bal}")

print(f"Total: {}")
print(f"Average: {}")
# AVERAGE: total of items / number of items


# running_total = running_total + new_amount
# running_total += new_amount

