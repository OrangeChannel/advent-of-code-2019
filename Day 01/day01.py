"""20.6ms"""
from math import floor

f = open('day01_input.txt')


def fuel(x):
    return floor(int(x) / 3) - 2


print('Part 1: {}'.format(sum([fuel(i) for i in f])))

f.seek(0)  # reset position in file object

module_fuels = []
for key, module_weight in enumerate(f):
    if fuel(module_weight) > 0:
        module_fuels.append(fuel(module_weight))
        curr_fuel = fuel(module_weight)

        while fuel(curr_fuel) > 0:
            curr_fuel = fuel(curr_fuel)  # recursively add fuel
            module_fuels[key] += curr_fuel

print('Part 2: {}'.format(sum(module_fuels)))
