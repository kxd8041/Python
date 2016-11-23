"""
Author: Krishna Teja Duggirala
Program: Find the anagrams present in the given list
"""

def anagram(x):
    result =[]
    l =len(x)-1
    while l > -1:
        for i in range(0,len(x)):
            if i==l:
                pass
            else:
                if fsort(x[i]) == fsort(x[l]):
                    if (x[i]) in result:
                        pass
                    else:
                        result.append(x[i])
                    if (x[l]) in result:
                        pass
                    else:
                        result.append(x[l])

        l=l-1
    print result


def fsort(i):
    ls =[]
    a = ''
    l = len(i)
    for j in range(0,l):
        ls.append(i[j])

    for i in range(0, l-1):
       for j in range(0,l-1):
        if ord(ls[j]) > ord(ls[j+1]):
            a = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = a
    val= ''.join(ls)
    return val








x=["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(x)


