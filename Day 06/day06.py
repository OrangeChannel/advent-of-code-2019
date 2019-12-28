l = [line.rstrip().split(')') for line in open('input.txt')]
centers, orbiters, parents = [i[0] for i in l], [i[1] for i in l], {}

# ----------------------------------- Part 1 --------------------------------- #
for k, v in enumerate(orbiters): parents[v] = centers[k]

def travel(pset, ckey, sset=None, d=1):
    if sset is not None:  # part 1
        if pset[ckey] in pset.keys():
            sset[pset[ckey]] = d - 1
            return travel(pset, pset[ckey], sset, d + 1)
        else: return sset
    if pset[ckey] in pset.keys(): return travel(pset, pset[ckey], d=d + 1)
    else: return d

print('Part 1: {}'.format(sum(travel(parents, v) for v in parents.keys())))

# ----------------------------------- Part 2 --------------------------------- #
a, b = travel(parents, 'YOU', {}), travel(parents, 'SAN', {})

print('Part 2: {}'.format(min([a[i] + b[i] for i in (a.keys() & b.keys())])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 314247
# Part 2: 514

# Time (mean ± σ):      86.9 ms ±   1.2 ms    [User: 84.3 ms, System: 2.6 ms]
# Range (min … max):    85.3 ms …  90.5 ms    33 runs


# ----------------------------------- Notes ---------------------------------- #
# def paths(d, clist, t=0):
#   for c in clist: t = t + len(d[c]) + paths(d, d[c]) if c in d.keys() else t
#   return t

# def count(pset, ckey, dist=1):
#   if pset[ckey] in pset.keys(): return count(pset, pset[ckey], dist + 1)
#   else: return dist

# original algorithms for part 1+2
# part 1 used a `children` dict instead of the `parents` dict used by part 2
# ~11% speedup by combining both to use same dict
