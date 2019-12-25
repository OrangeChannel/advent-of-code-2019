# ----------------------------------- Part 1 --------------------------------- #
from math import floor
from typing import Union

file = open('input.txt')


def fuel(weight: Union[str, int]):
    return floor(int(weight) / 3) - 2


print('Part 1: {}'.format(sum([fuel(line) for line in file])))

# ----------------------------------- Part 2 --------------------------------- #
file.seek(0)  # reset position in file object


def recursive_fuel(total_weight: Union[str, int]):
    if fuel(total_weight) > 0:
        return fuel(total_weight) + recursive_fuel(fuel(total_weight))
    else:
        return 0


print('Part 2: {}'.format(sum([recursive_fuel(line) for line in file])))

# ----------------------------------- Output --------------------------------- #
# Part 1: 3262358
# Part 2: 4890696
