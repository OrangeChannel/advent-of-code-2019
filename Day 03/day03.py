# ----------------------------------- Part 1 --------------------------------- #
file = open('input.txt')
awire = file.readline().split(',')
bwire = file.readline().split(',')
dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dy = {'L': 0, 'R': 0, 'D': -1, 'U': 1}


def points(ilist: list, x=0, y=0, acc=0):
    pointlist = {}

    for instruction in ilist:
        direction = instruction[0]
        length = int(instruction[1:])

        for i in range(1, length + 1):
            x += dx[direction]
            y += dy[direction]

            if (x, y) not in pointlist:
                pointlist[(x, y)] = acc + i

        acc += length

    return pointlist


apoints = points(awire)
bpoints = points(bwire)
common_points = apoints.keys() & bpoints.keys()

dists = [abs(x) + abs(y) for (x, y) in common_points]

print('Part 1: {}'.format(min(dists)))

# ----------------------------------- Part 2 --------------------------------- #
paths = [apoints[i] + bpoints[i] for i in common_points]

print('Part 2: {}'.format(min(paths)))

# ----------------------------------- Output --------------------------------- #
# Part 1: 225
# Part 2: 35194
