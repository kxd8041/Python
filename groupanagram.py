"""
Author: Krishna Teja Duggirala
Program: Find the anagrams present in the given list and group them.
"""
def groupAnagrams(x):

    d = {}
    for i in x:
        s = ''.join(fsort(i))
        d.setdefault(s, [])
        d[s] += [i]
    return d.values()

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
print groupAnagrams(x)

