"""
# Author :Krishna teja
# Program to print a list of numbers that are divisors of the number num taken from user
"""


#initializing a list for output
final = []

#getting the value num from user
num = raw_input("Please input a number :")
num = int(num) #typecsting into int

# Initialising the for loop to iterate from 1 till num+1
for i in range(1,num+1):
    if (num%i == 0): #checking if the mod value is equal to 0
        final.append(i)

print "Divisore List =", final