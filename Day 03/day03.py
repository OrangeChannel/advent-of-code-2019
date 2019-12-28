file = open('input.txt')
awire, bwire = file.readline().split(','), file.readline().split(',')

# ----------------------------------- Part 1 --------------------------------- #
dx, dy = {'L': -1, 'R': 1, 'U': 0, 'D': 0}, {'L': 0, 'R': 0, 'D': -1, 'U': 1}

def points(ilist: list, x=0, y=0, acc=0):
    pointlist = {}

    for instruction in ilist:
        direction, length = instruction[0], int(instruction[1:])

        for i in range(1, length + 1):
            x, y = x + dx[direction], y + dy[direction]
            if (x, y) not in pointlist: pointlist[(x, y)] = acc + i

        acc += length

    return pointlist

common = (apoints := points(awire)).keys() & (bpoints := points(bwire)).keys()

print('Part 1: {}'.format(min([abs(x) + abs(y) for (x, y) in common])))

# ----------------------------------- Part 2 --------------------------------- #
print('Part 2: {}'.format(min([apoints[i] + bpoints[i] for i in common])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 225
# Part 2: 35194

# Time (mean ± σ):     153.9 ms ±   1.1 ms    [User: 132.3 ms, System: 21.5 ms]
# Range (min … max):   152.9 ms … 157.4 ms    19 runs
