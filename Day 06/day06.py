# ----------------------------------- Part 1 --------------------------------- #
l = [line.rstrip().split(')') for line in open('input.txt')]
centers, orbiters, children= [i[0] for i in l], [i[1] for i in l], {}
for k, v in enumerate(orbiters):
    children.setdefault(centers[k], []).append(v)


def path(s, clist, t=0):
    for child in clist:
        t = t + len(s[child]) + path(s, s[child]) if child in s.keys() else t
    return t


sub_orbits = sum(path(children, v) for v in children.values())
root_orbits = path(children, ['COM'])
print('Part 1: {}'.format(sub_orbits + root_orbits))

# ----------------------------------- Part 2 --------------------------------- #
