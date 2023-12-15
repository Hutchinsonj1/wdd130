with open("hr_system_file.txt") as hr_system:
    for line in hr_system:
        clean_line = line.strip()
        line_parts = clean_line.split(" ")
        id = line_parts[1]
        job_title = line_parts[2]
        salary = float(line_parts[3])
        names = []
        name = line_parts[0]
        print(name)
