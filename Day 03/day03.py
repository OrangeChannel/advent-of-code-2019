import math
# awire = open('day03_input.txt').readlines()[0].rstrip().split(',')
# bwire = open('day03_input.txt').readlines()[1].rstrip().split(',')
awire = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
bwire = ['U62','R66','U55','R34','D71','R55','D58','R83']
awire = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
bwire = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

dx = {'L': -1, 'R': 1}
dy = {'D': -1, 'U': 1}


def points(l: list):
    pointlist = []
    x, y, t = 0, 0, 0
    for _ in l:
        if _[0] in dx.keys():
            for i in range(1, int(_[1:]) + 1):
                x += dx[_[0]]
                t+=1
                pointlist.append((x, y, t))
        elif _[0] in dy.keys():
            for i in range(1, int(_[1:]) + 1):
                y += dy[_[0]]
                t+=1
                pointlist.append((x, y, t))
    return pointlist

afull = points(awire)
bfull = points(bwire)
afulls = afull[:]
bfulls = bfull[:]
afulls.sort()
bfulls.sort()
apoints = [i[:2] for i in afulls]
bpoints = [i[:2] for i in bfulls]
common, common_a, common_b = [], [], []
for k,v in enumerate(apoints):
    if v in bpoints:
        common.append(v)
        # if k < min(len(afull), len(bfull)):
        #     common_a.append(afull[k])
        #     common_b.append(bfull[k])
dists = []
for i in common:
    dists.append(math.fabs(i[0])+math.fabs(i[1]))
print(min(dists))
