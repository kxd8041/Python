
"""
# Author :Krishna teja
# Program to find the sum of three numbers and also if the given numbers are equal then return thrice of their sum.
"""

# Getting the input from the user
var1, var2, var3 = raw_input("enter three numbers:").split(' ')

#converting the type
ans = (int(var1)+int(var2)+int(var3))

#checking if all the given 3 numbers are same
if (var1==var2==var3):
    print int(ans) * 3
else:
    print ans