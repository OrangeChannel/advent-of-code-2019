import more_itertools

data = open('input.txt').readline().rstrip()
length, height = 25, 6
layer_size = length * height

slicer = more_itertools.grouper(data, layer_size)

layers = {}
for i in range((num_layers := int(len(data)/layer_size))):
    layers[i] = next(slicer)

num_zeroes = {}
for i in range(num_layers):
    num_zeroes[i] = layers[i].count('0')

min_zeroes = min(num_zeroes.values())
for key in num_zeroes.keys():
    if min_zeroes == num_zeroes[key]:
        goal = key

print('Part 1: {}'.format(layers[goal].count('1') * layers[goal].count('2')))

# ----------------------------------- Part 2 --------------------------------- #

picture = []
for k,v in enumerate(layers[(curr := 0)]):
    picture.append(v)

while '2' in picture:
    for k,v in enumerate(picture):
        if v == '2':
            picture[k] = layers[curr + 1][k]
    curr += 1

rows = []
rowcutter = more_itertools.grouper(picture, length)
for i in range(height):
    rows.append(next(rowcutter))

print('Part 2:\n' + u'\u2588' * (2 * length + 2))

for r in range(height):
    t = u'\u2587'
    for v in range(length):
        t += ''.join(rows[r][v]) + ''.join(rows[r][v])
    t = t.replace('0', u'\u2587')
    t = t.replace('1', ' ') + u'\u2587'
    print(t)

print(u'\u2588' * (2 * length + 2))

# ----------------------------------- Output --------------------------------- #
# Part 1: 1950
# Part 2:
# ████████████████████████████████████████████████████
# ▇        ▇▇  ▇▇▇▇  ▇▇▇▇    ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇▇
# ▇  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇▇
# ▇      ▇▇▇▇    ▇▇▇▇▇▇  ▇▇▇▇  ▇▇        ▇▇  ▇▇▇▇▇▇▇▇▇
# ▇  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇        ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇▇
# ▇  ▇▇▇▇▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇▇▇▇▇▇
# ▇  ▇▇▇▇▇▇▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇  ▇▇▇▇  ▇▇        ▇▇▇
# ████████████████████████████████████████████████████

# Time (mean ± σ):      20.9 ms ±   0.3 ms    [User: 17.5 ms, System: 3.3 ms]
# Range (min … max):    20.3 ms …  21.6 ms    124 runs

# ----------------------------------- Notes ---------------------------------- #
# This is horribly inefficient, ugly, and dumb but it works ;)
