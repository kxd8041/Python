####
# Author :Krishna teja
# Program to find if a given string is palindrome or not
####


s1 = raw_input("Please enter the string to check for palindrome :")
# Getting the raw input from the user

# creating a method to check if the passed string is palindrome or not.
def is_palindrome(str):
    s2=s1.lower()
    s3=s2[::-1] #using the slice operator to reverse the string
    if(s2==s3):
        print "Yes, it is a palindrome"
    else:
        print "No, it is not a palindrome"

    return

is_palindrome(s1) #calling the method 