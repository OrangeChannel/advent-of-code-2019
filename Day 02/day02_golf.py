"""
4 chars, 11 lines, 494ms
things wrong with this solution:
- won't print part 2 if same values as (12,2) from part 1
- doesn't check for incorrect optcodes, nor incorrect length of list
- hugely inefficient brute force method with no break once solution is found
"""
def i(l):
    for k in range(0, len(l), 4):
        if l[k] == 99: break
        if l[k] == 1: l[l[k + 3]] = l[l[k + 1]] + l[l[k + 2]]
        elif l[k] == 2: l[l[k + 3]] = l[l[k + 1]] * l[l[k + 2]]
    return l[0]
for (o, p) in [(o,p) for o in range(100) for p in range(100)]:
    n = [int(_) for _ in list(open('2'))[0].split(',')]
    n[1:3] = [o, p]
    if (o, p) == (12, 2): print(i(n))
    elif i(n) == 19690720: print(100 * o + p)
