
with open("courses.txt") as courses_file:
    for line in courses_file:
        # line = ["CSE 130", "98.5"] It views everything on a line as ONE thing
        line = line.strip()
        line = line.split(",")
        name = line[0]
        grade = float(line[1])
        bonus_grade = grade + 3
        # grade = grade.strip()
        print(f"{name} - Grade: {grade}, with Bonus: {bonus_grade}")
print("The file is now closed.\n")
    
# STRIP = Whitespace on ENDS
# SPLIT = Split string/file into PARTS