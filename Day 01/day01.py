file = open('input.txt')

# ----------------------------------- Part 1 --------------------------------- #
fuel = lambda weight: int(weight) // 3 - 2

print('Part 1: {}'.format(sum([*map(fuel, file)])))

# ----------------------------------- Part 2 --------------------------------- #
file.seek(0)  # reset position in file object

def recursive_fuel(total):
    if fuel(total) > 0: return fuel(total) + recursive_fuel(fuel(total))
    else: return 0

print('Part 2: {}'.format(sum([*map(recursive_fuel, file)])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 3262358
# Part 2: 4890696

# Time (mean ± σ):      16.1 ms ±   0.1 ms    [User: 13.4 ms, System: 2.8 ms]
# Range (min … max):    15.9 ms …  16.8 ms    163 runs
