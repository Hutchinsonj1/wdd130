# def name():
#     initials = name[0:1]
#     print(name)
#     return initials

# # name = input("What is the name: ")
# initials = 
# print(f"The name is {name}")

from datetime import datetime

print("Task completed")
print(datetime.now())
print()

for x in range(0,10):
    print(x)
print()
print("Second task completed")
print(datetime.now())
print()

# OR

def function(task_name):
    print(task_name)
    print(datetime.now())
    print()

function("Task completed")

for y in range(10):
    print(y)
# print("Second task completed. End of function ?")
function("End of loop")
print()




# first_name = input("Enter your first name: ")
# first_initial = first_name[0:1]

# last_name = input("Enter your last name: ")
# last_initial = last_name[0:1]

# print(first_initial + last_initial)
# print()


def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

get_initial()

first_name_initial = get_initial(first_name[0:1])
last_name_initial = get_initial(last_name[0:1])

print("The initials for your name are: " + first_name_initial \
      + last_name_initial)
# get_initial()


# This function will return the first initial of a Name
def message(name,force_uppercase=False,force_lowercase=False):
    if force_uppercase:
        inital = name.upper()
    elif force_lowercase:
        inital = name.lower()
    else:
        inital = name
    return inital

original_message = input("What is the message? ")

upper_message = message(original_message,force_uppercase=True)

lower_message = message(original_message,force_lowercase=True)

print(f"{original_message}\n{upper_message}\n{lower_message}")
print()

