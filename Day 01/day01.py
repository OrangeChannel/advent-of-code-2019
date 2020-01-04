file = [*map(int, open('input.txt'))]

# ----------------------------------- Part 1 --------------------------------- #
fuel = lambda weight: weight // 3 - 2

print('Part 1: {}'.format(sum([*map(fuel, file)])))

# ----------------------------------- Part 2 --------------------------------- #
recurse = lambda weight: f + recurse(f) if (f:=fuel(weight)) > 0 else 0

print('Part 2: {}'.format(sum([*map(recurse, file)])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 3262358
# Part 2: 4890696

# Time (mean ± σ):      16.2 ms ±   0.2 ms    [User: 13.3 ms, System: 2.9 ms]
# Range (min … max):    16.0 ms …  17.5 ms    162 runs
