"""
# Author :Krishna teja
# Program to get a string from user and then priting count of each word and letter
"""

string = raw_input("Please enter a string :")
s1 = string.split() #splitting the string to get each word
print len(s1)
print "words"
dict = {}
dict1 = {}

# looping through the count of words and checking if each word is present in the dictionary
# if present incrementing the value else creating a new entry with count 1
for i in range(0,len(s1)):
    if dict.has_key(s1[i]):
        result = dict.get(s1[i])+1
        dict[s1[i]] = result;
    else:
        dict[s1[i]] = 1;

# printing all the key value pairs
for key, value in dict.iteritems() :
    print key, value

# Replacing the spaces and also converting all the chars into lower case
string1 =string.replace(' ','')
string1 = string1.lower()

# Looping through the count of characters present in the string and
# performing same operation as the first for loop

for i in range(0,len(string1)):
    if dict1.has_key(string1[i]):
        result = dict1.get(string1[i])+1
        dict1[string1[i]] = result;
    else:
        dict1[string1[i]] = 1;


print "letters"
# Looping from 97 to 123 as they are the asci values of atoz and printing the values accordingly

for i in range(97,123):
    if dict1.has_key(chr(i)):
        print chr(i), dict1[chr(i)]
    else:
        print chr(i), 0

