# Create empty list, so I can put parts of each line in it, and iterate through
data_set = []

with open("books_and_chapters.txt") as books_and_chaps:
    for line in books_and_chaps:
        # strip whitespace off the ends:
        line = line.strip()
        # split my line into parts:
        parts = line.split(":")
        # Assign variables to those different parts
        book = parts[0]
        chapters = int(parts[1]) # Also changed type to "int" so I can work with numbers
        scripture = parts[2]
        # Putting parts of the line into an empty List (see at the top)
        data_set.append(parts)

        # To follow the Instructor, I copy and paste the format he wants:
        #   Scripture: Old Testament, Book: Genesis, Chapters: 50
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

# Making variables before I use them in the Loops below
max_chapters = 0
book_max_chap = ""
total_chaps = []
chapters_sum = 0

print()
for i in data_set:
    # Changing parts[1] to type "int", (i[1] is not changed automatically from above)
    i[1] = int(i[1])
    # Find the max chapters, and make sure I find the Book at the same time
    if i[1] > max_chapters:
        # When it finds the most chapters, I assign that Part (i[1]) to "max_chapters" (like x = 3)
        max_chapters = i[1]
        # Find the book Name at the same time, and be sure I assign it to a variable when I've found it
        book_max_chaps = i[0]

    # Entering the loop, by just saying the chapter number is greater than 0.
    if i[1] > 0:
        # Putting all chapters into a List (total_chaps)
        total_chaps.append(i[1])
        # Finding the total of all chapters put together
        chapters_sum = sum(total_chaps)

print(f"The book with the largest number of chapters is {book_max_chaps}, with {max_chapters} chapters")
print(f"The total chapters found in the standard works is {chapters_sum}\n")
