
"""
# Author :Krishna teja
# Program to return list with numbers less than x taken from user and
print a new list with elements less than number x.
"""

# storing the list
numbers = [1,2,2,3,4,55,65,76,78]

#initializing another list for output
final = []

# Sorting the list so as to reduce the time complexity
numbers.sort()

#getting the value x from user
x = raw_input("Please input a number :")

# getting the length of the list to iterate it
nl = len(numbers)

# Initialising the for loop to iterate from the start postion till the end
for i in range(0,nl):
    if (numbers[i]<int(x)): #checking if the current list value is less than x
        final.append(numbers[i])
    else:
        break # if the current value is greater than x, since the list is sorted, we can come out of the loop.

print final