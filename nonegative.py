"""
# Author :Krishna teja
# Program to define a function add_digits which continuosly adds digits untill the result is a single digit.
"""

def add_digit():
    n = raw_input("Please enter a non negative integer")
    while len(n)>1:
        result = 0
        for i in range(0,len(n)):
            result = result + int(n[i])
        n = str(result)
    print result


add_digit()