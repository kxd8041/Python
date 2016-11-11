"""
# Author :Krishna teja
# Program to get accustomed with input/output
"""

## part 1
st = raw_input("Please enter a string :")
l = len(st)
c =[]


for i in range(0,l):
    if st[i].isupper():
        c.append(st[i].lower())
    else :
        c.append(st[i].upper())

b = ''.join(c)
print b

### part 2

st = raw_input("Please enter a string :")
print st.replace(' ', '-')
