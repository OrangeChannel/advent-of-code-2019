l = [line.rstrip().split(')') for line in open('input.txt')]
centers, orbiters = [i[0] for i in l], [i[1] for i in l]

# ----------------------------------- Part 1 --------------------------------- #
children, parents = {}, {}

for k, v in enumerate(orbiters):
    children.setdefault(centers[k], []).append(v)
    parents[v] = centers[k]

def paths(d, clist, t=0):
    for c in clist: t = t + len(d[c]) + paths(d, d[c]) if c in d.keys() else t
    return t

sub_orbits = sum(paths(children, v) for v in children.values())
print('Part 1: {}'.format(sub_orbits + paths(children, ['COM'])))

# ----------------------------------- Part 2 --------------------------------- #
def travel(pset, ckey, sset=None, dist=0):
    if sset is None: sset = {}

    if pset[ckey] in pset.keys():
        sset[pset[ckey]] = dist
        return travel(pset, pset[ckey], sset, dist + 1)

    else: return sset

a, b = travel(parents, 'YOU'), travel(parents, 'SAN')
print('Part 2: {}'.format(min([a[i] + b[i] for i in (a.keys() & b.keys())])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 314247
# Part 2: 514

# Time (mean ± σ):      97.8 ms ±   0.7 ms    [User: 94.3 ms, System: 3.2 ms]
# Range (min … max):    96.6 ms …  99.5 ms    30 runs


# ----------------------------------- Notes ---------------------------------- #
# travel() doesn't reach 'COM' because 'COM' has no parents
