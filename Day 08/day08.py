from more_itertools import grouper
from itertools import product
data, length, height = open('input.txt').readline().rstrip(), 25, 6

# ----------------------------------- Part 1 --------------------------------- #
slicer = grouper(data, (size := length * height))
(layers := [(i, next(slicer)) for i in range(len(data) // size)]).sort(key=lambda l: l[1].count('0'))

print('Part 1: {}'.format((g := layers[0][1]).count('1') * g.count('2')))

# ----------------------------------- Part 2 --------------------------------- #
picture, curr = [list(l[1]) for l in sorted(layers)], 0

while '2' in (out := picture[0] if curr == 0 else out):  # only defined first time
    for k, v in enumerate(out):
        if v == '2': out[k] = picture[curr + 1][k]
    curr += 1

print('Part 2:\n' + u'\u2588' * ((w := 2) * length + 2))

for r, c in product(range(height), range(length)):
    if c == 0: print(u'\u2588' * w, end='')
    print(' ' * w if out[r * length + c] == '1' else u'\u2587' * w, end='')
    if c == length - 1: print('')
    if r == height - 1 and c == length - 1: print(u'\u2588' * (w * length + 2))

# ----------------------------------- Output --------------------------------- #
# Part 1: 1950
# Part 2:
# ████████████████████████████████████████████████████
# ██        ▇▇  ▇▇▇▇  ▇▇▇▇    ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇
# ██  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇
# ██      ▇▇▇▇    ▇▇▇▇▇▇  ▇▇▇▇  ▇▇        ▇▇  ▇▇▇▇▇▇▇▇
# ██  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇        ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇
# ██  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇
# ██  ▇▇▇▇▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇        ▇▇
# ████████████████████████████████████████████████████

# Time (mean ± σ):      20.5 ms ±   0.1 ms    [User: 17.3 ms, System: 3.3 ms]
# Range (min … max):    20.2 ms …  20.9 ms    131 runs
