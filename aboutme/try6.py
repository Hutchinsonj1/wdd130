tips_list = []
tips = 0
total = 0
print()
while tips != "quit":
    tips = input("What is the tip amount? ")
    if tips != "quit":
        tips = float(tips)
        # tips_list.append(tips)
        total = total + tips

print(total)
