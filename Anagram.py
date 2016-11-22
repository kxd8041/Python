"""
Author: Krishna Teja Duggirala
Program: Find the anagrams present in the given list
"""

def anagram(x):
    result =[]
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            if i == j:
                pass
            else:

                if sorted(x[i])==sorted(x[j]):
                    if (x[i])in result:
                        pass
                    else:
                       result.append(x[i])

                    if (x[j])in result:
                       pass
                    else:
                       result.append(x[j])


    print result



x=["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(x)


