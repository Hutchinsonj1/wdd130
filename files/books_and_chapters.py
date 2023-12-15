# close the file after, so we do "with open..."
data_set = []
user = input("Which volume of scriptures would you like to learn about (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, or Pearl of Great Price)? ").lower()

with open("C:/Users/Jadenhutchinson/Documents/byui/wdd130/files/books_and_chapters.txt") as books_and_chaps:
    for line in books_and_chaps:
        # print(line)
        line = line.strip()
        parts = line.split(":")
        book = parts[0]
        chapters = int(parts[1])
        scripture = parts[2]

        data_set.append(parts)

        # Scripture: Old Testament, Book: Genesis, Chapters: 50
        # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
# Most chapters in ALL scripture
max_chap = 0
book_max_chap = ""
# Most chapters in Book of Mormon
bom_max_chap = 0
bom_book_max_chap = ""

# Total chapters found in ALL scriture
total_chaps = []
chapters_sum = 0
print()
for i in data_set:
    i[1] = int(i[1])
    if i[1] > 0:
        total_chaps.append(i[1])
        chapters_sum = sum(total_chaps)
    if i[2] == "Book of Mormon":
        # print(i[0])-- prints Just the chaps in the BOM
        if i[1] > bom_max_chap:
            bom_max_chap = i[1]
            bom_book_max_chap = i[0]  #something = True
    if i[2] == "new testament":
        # print(i[0])-- prints Just the chaps in the BOM
        if i[1] > bom_max_chap:
            bom_max_chap = i[1]
            bom_book_max_chap = i[0]
    
    if i[1] > max_chap:
        max_chap = i[1]
        book_max_chap = i[0]

print(f"The book with the largest number of chapters is {book_max_chap}, with {max_chap} chapters.")
print(f"The book with the largest number of chapters in the Book of Mormon is {bom_book_max_chap}, with {bom_max_chap} chapters.")
print(f"The total chapters found in the standard works is {chapters_sum}.\n")
