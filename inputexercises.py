
"""
# Author :Krishna teja
# Program to explore input / output operations in python
"""


# Write a program asking for user's name and age (input and raw_input).
# Display a message conveying user the year that he will turn 80 years old.

# Getting the name from user
name = raw_input("Please input your name :")
# Getting the age from user
age = raw_input("Please input your age :")

# calculating the year
age = 80 - int(age)
age = 2016 + age

print "Hello",name,"you will become 80 years in the year", age


# Level 2
# Write a program asking user to enter a number, depending on whether the number is even or #odd, print out an appropriate message to the user.

num = raw_input("Please input a random number :")
if (int(num)%2==0):
    print "It is an even number"
else:
    print "It is an odd number"

if (int(num)%4==0):
    print " & It is a multiple of 4"

#level 3
# Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

num = raw_input("Please input a random number :")
num1 = raw_input("Please input a random number :")

if(int(num1)%int(num)==0):
    print "They are divisible"
else:
    print " They are not divisible"

