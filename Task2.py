
'''
Task 2: Create a Personalized Greeting Problem Statement: Write a Python program that:
'''
#Takes a user's first name and last name as input.

print("Enter your First name ")
a=input()
print ("Enter your last name")
b= input()

#Concatenated the first name and last name into a full name.

c= a+" "+b

#Printed a personalized greeting message using the full name.

print ("Hello, {} ! Welcome to the python program.".format(c))