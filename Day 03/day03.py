""" 157 ms """
awire = open('day03_input.txt').readlines()[0].rstrip().split(',')
bwire = open('day03_input.txt').readlines()[1].rstrip().split(',')
dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dy = {'L': 0, 'R': 0, 'D': -1, 'U': 1}


def points(l: list):
    pointlist = {}  # had to get a hint on this one, lists were too slow for part 2
    x, y, acc = 0, 0, 0
    for _ in l:
        d = _[0]
        n = int(_[1:])
        for i in range(1, n + 1):
            x += dx[d]
            y += dy[d]
            if (x, y) not in pointlist:  # only include the distance for the first time the wire hits point (x,y)
                pointlist[(x, y)] = acc + i
        acc += n  # avoid increasing length for each move, 7% performance increase with this particular input
    return pointlist


apoints = points(awire)
bpoints = points(bwire)
common = set(apoints.keys()) & set(bpoints.keys())
print('Part 1: {}'.format(min([abs(x) + abs(y) for (x, y) in common])))
print('Part 2: {}'.format(min([apoints[i] + bpoints[i] for i in common])))
