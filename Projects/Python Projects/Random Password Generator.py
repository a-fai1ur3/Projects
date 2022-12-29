# this is the random password generator with different combinations
# 

import random # library

# we have a variable characters
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_" # string format

while True : # nested loops , while loop
    pass_length = int(input("Enter the Length of Required Password: ")) # variable for length of password
    pass_count = int(input("Enter the Number of Required Passwords: ")) # variable for count of password
# nested loop, for loop
    for i in range(0, pass_count):
        password = "" # empty string
        for j in range (0, pass_length):
            pass_char = random.choice(characters)
            password = password+pass_char 

        print("The Generated Password is", password)
    repeat = input("Do you want to Generate more Passwords with Different Combinations? ") # variable
    if repeat == "no" or repeat == "No":
        break
print ("Thank You for Using this Password Generator!")

# add more code for password only greater then 6 length 
# add else statment for taking yes or Yes else move to error.