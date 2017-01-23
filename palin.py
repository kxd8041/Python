"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

"""
class palin(object):

    def ispalin(y):
        l=len(y)
        mismatch = 0
        bool = False
        if l%2==0:
            la = len(y)-1
            for i in range(0,l):
                if i!=la:
                    if y[i]==y[la]:
                        bool = True
                    else:
                        bool = False
                        mismatch = mismatch+1
            if bool== False : print mismatch
            else : print '0'

        else:
            la = len(y) - 1
            bool = False
            for i in range(0, l):
                if i!=la:
                    if y[i] == y[la]:
                        bool = True
                    else:
                        mismatch = mismatch + 1
            if bool == False:
                print mismatch-1
            else:
                print '0'

    y=raw_input()
    ispalin(y)

