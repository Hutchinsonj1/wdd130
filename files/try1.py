people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 9999
youngest_person = ""
# Vars to find average (3):
ages = []
total_ages = 0
age_avg = 0

for line in people:
    parts = line.split(" ")
    # parts[1] = int(parts[1])
    name = parts[0]
    age = parts[1]
    # print(parts[1])

    # ages.append(age)
    # total_ages = sum(ages)
    # age_avg = total_ages / len(ages)

    if age < youngest:
        youngest = age
        youngest_person = name

# print(f"\nThe average age is {age_avg:.2f}")
print(f"\nThe youngest person is {youngest_person}, whose age is {youngest}.\n")
