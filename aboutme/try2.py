numbers = [1,2,3,4,5,6,7]
for i in numbers:
    print(i)

colors = ["red","blue","green"]
for j in colors:
    print(j)

for i in range(1,11):
    print(i)

for j in range(10000,100000,10000):
    print(f"{j:.2f}")

f_name = "Jaden"
third_letter = f_name[2]
print(third_letter)

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")


word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    print(index)

first_name = "Brigham"
number_of_letters = 7
for letter in range(number_of_letters):
    l = first_name[number_of_letters]
    print(letter)

# Using LEN
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")



word = "book"
number_of_letters = len(word) # Notice this can now work for any string

for i in range(number_of_letters):
    letter = word[i]
    print(f"Index: {i} Letter: {letter}")


word = input()
number_of_letters = len(word)

for i in range(number_of_letters):
    letter = word[i]
    print(f"Index: {i} Letter: {letter}")





first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")


# for i in __
#word[index]