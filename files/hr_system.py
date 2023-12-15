with open("hr_system_file.txt") as hr_system:
    for line in hr_system:
        clean_line = line.strip()
        line_parts = clean_line.split(" ")
        name = line_parts[0]
        id = line_parts[1]
        job_title = line_parts[2]
        salary = float(line_parts[3])
        length = len(name)
        print(line_parts)

        paycheck = salary / 24
        # print(line_parts)

        # if job_title.lower() == "engineer":
        #     paycheck += 1000
        #     print(f"{name} (ID: {id}), {job_title} - ${paycheck:.2f}")
        # else:
        #     print(f"{name}, ID:{id}, {job_title}, {paycheck:.2f}")
