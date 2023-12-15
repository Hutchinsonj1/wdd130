t_amount = []
running_total = 0
accounts = []
new_account = ""

run_program = False
while(not run_program):
    new_account = input("What is the name of the account? ").lower()
    amount = int(input("What is the balance? "))
    if new_account != "quit".lower():
            accounts.append(new_account)
    else:
        run_program = True
print()

for amount in t_amount:
    running_total  = running_total + t_amount

for account in accounts:
    balance = account[t_amount]
    print(f"{account} - ${balance:.2f}")
    # print(client)




# print(f"The running total is {running_total:.2f}")

# word = input()
# number_of_letters = len(word)

# for i in range(number_of_letters):
#     letter = word[i]
#     print(f"Index: {i} Letter: {letter}")