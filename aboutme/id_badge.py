"""
File: id_badge.py
Author: Jaden Hutchinson

This program will make an ID Badge!!

Purpose: To practice formatting strings.
"""

print("What is your first name?")
f_name = input();
print("What is your last name?")
l_name = input();
print("What is your email address?")
email = input();
print("What is your phone number?")
phone = input();
print("What is your job title?")
job_title = input();
print("What is your ID number?")
id_number = input();

print("\n")
print("Please enter the following information:" "\n")

print("First name: "+"\033[4m"+ f_name + "\033[0m")
print("Last name: "+"\033[4m"+ l_name + "\033[0m")
print("Email address: "+"\033[4m"+ email + "\033[0m")
print("Phone number: "+"\033[4m"+ phone + "\033[0m")
print("Job title: "+"\033[4m"+ job_title + "\033[0m")
print("ID number: "+"\033[4m"+ id_number + "\033[0m")
print()

print("The ID Card is: ")
print("----------------------------------------")
print(f"{l_name.upper()}, {f_name.title()}")
print(job_title.title())
print("ID number: "+ id_number)
print()
print(email.lower())
print(phone)
print("----------------------------------------")
print("\n")
