l, parents = [line.rstrip().split(')') for line in open('input.txt')], {}
for k, v in enumerate([i[1] for i in l]): parents[v] = [i[0] for i in l][k]
def dst(pset, ckey, dist_dict=None, d=1):
    if (parent := pset[ckey]) in pset.keys():
        if dist_dict is not None: dist_dict[parent] = d - 1  # part 1
        return dst(pset, parent, dist_dict, d=d + 1)  # part 1+2
    return dist_dict if dist_dict else d  # part 1 else part 2
a, b = dst(parents, 'YOU', {}), dst(parents, 'SAN', {})
print(sum(dst(parents, k) for k in parents.keys()), min([a[i] + b[i] for i in a.keys() & b.keys()]))
