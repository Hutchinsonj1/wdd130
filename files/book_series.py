with open("C:/Users/Jadenhutchinson/Documents/byui/wdd130/files/book_series.txt") as book_series:
    print()
    for line in book_series:
        line = line.strip()
        print(line)
    print("End of loop")
    print()

    