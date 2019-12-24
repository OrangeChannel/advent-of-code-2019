""" 459 chars, 15 lines """
def check(part):
    rlist = []
    for i in range(147981, 691423):
        if sorted(a := list(str(i))) == a:
            for char in a:
                (b := a[:]).remove(char)
                if char in b:
                    if part == 1:
                        rlist.append(i)
                        break
                    if b.count(char) == 1:
                        rlist.append(i)
                        break
    return len(rlist)
print(check(1), check(2))
