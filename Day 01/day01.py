# ----------------------------------- Part 1 --------------------------------- #
file = open('input.txt')
fuel = lambda weight: int(weight) // 3 - 2

print('Part 1: {}'.format(sum([*map(fuel, file)])))

# ----------------------------------- Part 2 --------------------------------- #
file.seek(0)  # reset position in file object


def recursive_fuel(total_weight):
    if fuel(total_weight) > 0:
        return fuel(total_weight) + recursive_fuel(fuel(total_weight))
    else:
        return 0


print('Part 2: {}'.format(sum([*map(recursive_fuel, file)])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 3262358
# Part 2: 4890696
