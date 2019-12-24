awire = open('day03_input.txt').readlines()[0].rstrip().split(',')
bwire = open('day03_input.txt').readlines()[1].rstrip().split(',')
# awire = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
# bwire = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
# awire = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
# bwire = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dy = {'L': 0, 'R': 0, 'D': -1, 'U': 1}


def points(l: list):
    pointlist = {}  # had to get a hint on this one, lists were too slow for part 2
    x, y, t = 0, 0, 0
    for _ in l:
        for i in range(int(_[1:])):
            x += dx[_[0]]
            y += dy[_[0]]
            t += 1
            if (x, y) not in pointlist:  # only include the distance for the first time the wire hits point (x,y)
                pointlist[(x, y)] = t
    return pointlist


apoints = points(awire)
bpoints = points(bwire)
common = set(apoints.keys()).intersection(set(bpoints.keys()))  # much faster than looping over lists to check for common points
print('Part 1: {}'.format(min([abs(x) + abs(y) for (x, y) in common])))
print('Part 2: {}'.format(min([apoints[i] + bpoints[i] for i in common])))
