
st = raw_input("Please enter a string")
l = len(st)
li = []

i = -1


if l%2 == 0:

    while i < l:
        i=i+1
        if i == l - 1:
            li.append((st[i], 1))
            break

        if st[i] == st[i+1]:
            li.append((st[i],2))
            i=i+1
        else:
            li.append((st[i],1))

    print li
else :
    while i < l:
        i = i + 1

        if i == l - 2:
            if st[i] == st[i+1]:
                li.append((st[i], 2))
            else:
                li.append((st[i],1))
                li.append((st[i+1],1))
            break

        if st[i] == st[i + 1]:
            li.append((st[i], 2))
            i = i + 1
        else:
            li.append((st[i], 1))

    print li