"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
"""
class filecounter(object):

    def __init__(self):
        self

    def filewordcount(self):
        f = open('text.txt', 'r')
        sum = 0
        wordcount=0


        for each in f.read().split():
                sum =  sum+len(each)
                wordcount=wordcount+1
        avg = sum/wordcount

        print "The average word length of the file is",avg

    filewordcount(1)