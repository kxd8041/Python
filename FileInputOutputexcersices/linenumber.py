"""
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""


class filecounter(object):

    def __init__(self):
        self


    def counter(self):
        f1= open("output.txt","w+")
        c = 1

        with open('text.txt', 'r') as openfileobject:
            for line in openfileobject:
                new = str(c)+". "+ line
                f1.write(new)
                c=c+1


    counter(1)