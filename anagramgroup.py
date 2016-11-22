"""
Author: Krishna Teja Duggirala
Program: Find the anagrams present in the given list and group them.
"""
def groupAnagrams(x):

    d = {}
    for i in x:
        s = ''.join(sorted(i))
        d.setdefault(s, [])
        d[s] += [i]
    return d.values()

x=["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(x)