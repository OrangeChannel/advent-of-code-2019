bottom = 147981
top = 691423
numlist = []
for i in range(bottom, top+1):
    a = list(str(i))
    if sorted(a) == a:
        for char in a:
            b = a[:]
            b.remove(char)
            if char in b:
                numlist.append(i)
                break
print('Part 1: {}'.format(len(numlist)))

numlist_b = []
for i in range(bottom, top+1):
    a = list(str(i))
    if sorted(a) == a:
        for char in a:
            b = a[:]
            b.remove(char)
            if char in b:
                if b.count(char) > 1:
                    continue
                if b.count(char) == 1:
                    numlist_b.append(i)
                    break
print('Part 2: {}'.format(len(numlist_b)))
