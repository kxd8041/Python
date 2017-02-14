class Multiple3(object):

    def __init__(self):
        print "Welcome"

    def Multiple3check(self,value):
            decimal = 0
            for each in value:
                decimal = decimal * 2 + int(each)
            print "The Given decimal number is :",decimal
            if decimal%3==0:
                print 1
            else:
                print 0


m = Multiple3()
number = int(raw_input("Please Input the number of testcases :"))

for i in range(number):
    value = raw_input("Please Input the binary number :")
    m.Multiple3check(value)


