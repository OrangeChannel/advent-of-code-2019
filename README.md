```py
# Day 1
print(sum([(c := lambda m: int(m) // 3 - 2)(i) for i in [i for i in open('1')]]), sum([(p := lambda m: c(m) + p(c(m)) if c(m) > 0 else 0)(i) for i in [i for i in open('1')]]))
# Day 2
from itertools import *
def i(l):
    for k in range(0, len(l), 4):
        if l[k] == 99: break
        if l[k] == 1: l[l[k + 3]] = l[l[k + 1]] + l[l[k + 2]]
        elif l[k] == 2: l[l[k + 3]] = l[l[k + 1]] * l[l[k + 2]]
    return l[0]
for o, p in product(range(100), repeat=2):
    n = [int(_) for _ in list(open('2'))[0].split(',')]
    n[1:3] = [o, p]
    if (o, p) == (12, 2): print(i(n))
    elif i(n) == 19690720: print(100 * o + p)
# Day 3
a, b, c, d, h = open('3').readlines()[0].rstrip().split(','), open('3').readlines()[1].rstrip().split(','), {'L': -1, 'R': 1, 'U': 0, 'D': 0}, {'L': 0, 'R': 0, 'D': -1, 'U': 1}, lambda x, y: set(x.keys()) & set(y.keys())
def f(l):
    p, x, y, t = {}, 0, 0, 0
    for _, i in [(_, i) for _ in l for i in range(int(_[1:]))]:
        x, y, t = x + c[_[0]], y + d[_[0]], t + 1
        if (x, y) not in p: p[(x, y)] = t
    return p
print(min([abs(x) + abs(y) for (x, y) in h(f(a), f(b))]), min([f(a)[i] + f(b)[i] for i in h(f(a), f(b))]))
```