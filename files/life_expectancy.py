data_set = []

interest_year = int(input("\nEnter the year of interest: "))

with open("C:/Users/Jadenhutchinson/Documents/byui/wdd130/files/life_expectancy.csv") as life_expectancy:
    for line in life_expectancy:
        row = line.split(",")
        row[2] = int(row[2]) # access row at POSITION "2"
        row[3] = float(row[3])
        
        data_set.append(row)

# min max
max_exp = 0
country = ""
year = 0
for j in data_set:
    if j[3] > max_exp:
        max_exp = j[3]
        country = j[0]
        year = j[2]

print(f"\nThe overall max life expectancy is: {max_exp} from {country} in {year}")

min_exp = 1000
country = ""
year = 0
for i in data_set:
    if i[3] < min_exp:
        min_exp = i[3]
        country = i[0]
        year = i[2]
print(f"\nThe overall min life expectancy is: {min_exp} from {country} in {year}\n")
# START AT 22:30

min_exp = 1000
max_exp = 0
interest_year = int(interest_year)
min_country = ""
max_country = ""
all_count = []
interest_count = []
# Average = add all the life exp and divide by the Number
for k in data_set:
    all_count.append(k[3])
    all_total_life_exp = sum(all_count)
    all_average_life_exp = all_total_life_exp / len(all_count)

    if k[2] == interest_year:
        if k[3] > max_exp:
            max_exp = k[3]
            max_country = k[0]
        if k[3] < min_exp:
            min_exp = k[3]
            min_country = k[0]
        # Finding the Average:
        interest_count.append(k[3])
        total_life_exp = sum(interest_count)
        average_life_exp = total_life_exp / len(interest_count)

print(f"The average life expectancy of all countries, across all years is {all_average_life_exp:.2f}\n")
print(f"For the year {interest_year}:")
print(f"The average life expectancy across all countries was {average_life_exp:.2f}")
print(f"The max life expectancy was in {max_country} with {max_exp:.2f}")
print(f"The min life expectancy was in {min_country} with {min_exp:.2f}\n")
print(f"Thanks for playing! Play again!\n")

        # interest_year = 
        # find the Interest year!
# print(data_set[0]) 


# print("The lowest life expectancy is:")
# print(data_set[7553][3])
# print()
# print("The highest life expectancy is:")
# print(data_set[11004][3])









        # my_list.append(fourth)
        # ['61.195']
#       print(my_list)

        # print(parts) = 
        # ['Zimbabwe', 'ZWE', '2019', '61.49']

        # fourth = parts[3]
        # my_list = []
        # my_list.append(fourth)
        # print(fourth)

        # print(first)
        # Zimbabwe (not in a list)

        # first_list = []
        # first_list.append(first)
        # print(first_list) = 
        # ['Zimbabwe']

        
        # parts = []
        # for i in parts:
        #     country = i[0]
        #     abrveviation = parts[1]
        #     year = parts[2]
        #     life_exp = parts[3]
# ['Zimbabwe', 'ZWE', '2018', '61.195']

        
        # clean_life = life_exp.strip()
        # clean_life = float(clean_life)

        # year.strip("\n")
        # year_exp_count = []
        # if year == "":
        #     pass
        # year_exp_count.append(parts[3])
        
        # print(year_exp_count)

#         [year_exp_count.extend(l) for l in (year)]
# print ("The extended and modified list is : " + str(year_exp_count))


        # last_list=[]
        # if p.last_name==None or p.last_name=="": 
        #     pass
        # last_list=last_list.append(p.last_name)
        # print last_list

        
        # if year_exp_count > 86.7:
        #     print(f"You found the highest life expectancy!: {year_exp_count}")
        # if clean_life < 17.8:
        #     print(f"You found the lowest life expectancy!: {year_exp_count}")

                
                
            
        