# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# first_name_initial = get_initial(first_name[0:1])
# last_name_initial = get_initial(last_name[0:1])
# print(f"Your initials are: {first_name_initial}{last_name_initial}")

def message_function(your_message,force_uppercase=False,force_lowercase=False,every_other=False):
    if force_uppercase:
        change_case = your_message.upper()
    elif force_lowercase:
        change_case = your_message.lower()
    # elif first:
    #     change_case[0:1].upper()
    # elif second:
    #     change_case[0:3].upper()
    return change_case

the_message = str(input("What is your message? "))
# messages = message_function(the_message)

upper_message = message_function(the_message,force_uppercase=True)

lower_message = message_function(the_message,force_lowercase=True)

print(f"{the_message}\n{upper_message}\n{lower_message}")
