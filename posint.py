"""
Author: Krishna Teja Duggirala
Program: Given an unsorted integer array, find the first missing positive integer.
"""

def posint():
    x =raw_input("Please enter digits for your array").split()
    x = map(int, x)
    x = sorted(x)
    y = 0
    c = 0
    for i in range(1,len(x)):
        y = (int(x[i])-1)
        if int(x[i-1]) < y:
            if (x[i-1]+1)>0:
                print "The first missing positive integer is :",x[i-1]+1
                c = 1

    if c == 0:
        print "The first missing positive integer is :",(int(x[-1])+1)



posint()