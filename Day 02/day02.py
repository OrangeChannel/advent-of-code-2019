# ----------------------------------- Part 1 --------------------------------- #
file = open('input.txt')
instruction_list = [*map(int, file.readline().split(','))]


def intcode(ilist: list):
    olist = ilist.copy()
    for k in range(0, len(olist), 4):
        opcode = olist[k]

        if opcode == 99:
            break

        elif opcode == 1:
            param1 = olist[olist[k + 1]]
            param2 = olist[olist[k + 2]]
            loc = olist[k + 3]
            olist[loc] = param1 + param2

        elif opcode == 2:
            param1 = olist[olist[k + 1]]
            param2 = olist[olist[k + 2]]
            loc = olist[k + 3]
            olist[loc] = param1 * param2

    return olist


instruction_list[1:3] = 12, 2
print('Part 1: {}'.format(intcode(instruction_list)[0]))

# ----------------------------------- Part 2 --------------------------------- #
from itertools import product

goal = 19690720
for noun, verb in product(range(100), repeat=2):
    instruction_list[1:3] = noun, verb

    if intcode(instruction_list)[0] == goal:
        print('Part 2: {}'.format(100 * noun + verb))
        break

# ----------------------------------- Output --------------------------------- #
# Part 1: 2782414
# Part 2: 9820
