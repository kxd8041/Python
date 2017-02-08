class circleLoop(object):
    def __init__(self):
        print "Welcome"

    def circle(self,n):
        for i in range(-n,n+1):
            for j in range(-n,n+1):

                 if (i * i + j * j <=  n * n) :
                    print "*",
                 else:
                    print ".",
            print " "


c = circleLoop()
n = int(raw_input("Please Input the circle radius :"))
c.circle(n)

