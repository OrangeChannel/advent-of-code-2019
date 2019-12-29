l = [line.rstrip().split(')') for line in open('input.txt')]
centers, orbiters, parents = [i[0] for i in l], [i[1] for i in l], {}

# ----------------------------------- Part 1 --------------------------------- #
for k, v in enumerate(orbiters): parents[v] = centers[k]

def travel(pset, ckey, sset=None, d=1):
    if (parent := pset[ckey]) in pset.keys():
        if sset is not None:  # part 1
            sset[parent] = d - 1
            return travel(pset, parent, sset, d + 1)
        return travel(pset, parent, d=d + 1)  # part 2
    return sset if sset else d

print('Part 1: {}'.format(sum(travel(parents, v) for v in parents.keys())))

# ----------------------------------- Part 2 --------------------------------- #
a, b = travel(parents, 'YOU', {}), travel(parents, 'SAN', {})

print('Part 2: {}'.format(min([a[i] + b[i] for i in (a.keys() & b.keys())])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 314247
# Part 2: 514

# Time (mean ± σ):      79.1 ms ±   0.6 ms    [User: 75.4 ms, System: 3.6 ms]
# Range (min … max):    77.7 ms …  80.4 ms    37 runs

# ----------------------------------- Notes ---------------------------------- #
# def paths(d, clist, t=0):
#   for c in clist: t = t + len(d[c]) + paths(d, d[c]) if c in d.keys() else t
#   return t

# def count(pset, ckey, dist=1):
#   if pset[ckey] in pset.keys(): return count(pset, pset[ckey], dist + 1)
#   else: return dist

# original algorithms for part 1+2
# part 1 used a `children` dict instead of the `parents` dict used by part 2
# ~19% speedup by combining both to use same dict
