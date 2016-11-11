"""
# Author :Krishna teja
# Program to print n number of stairs.
"""

st = raw_input("Please enter the number of stairs required :")
l = int(st)

for i in range(1,l+1):
        print ' ' * (l - i) + '#' * i

