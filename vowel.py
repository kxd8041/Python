####
# Author :Krishna teja
# Program to find if a given char is vowel or not
####

# Defining a method to check if the passed char is a vowel or not.

def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        print "It is not an vowel"
    else:
        print " It is a vowel"
    return

ch = raw_input("Please enter a character to check if it is an vowel :")
# Getting the raw input from the user

is_vowel(ch)
#calling the method 