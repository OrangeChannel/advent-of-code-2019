from itertools import product
instruction_list = [*map(int, open('input.txt').readline().split(','))]
goal = 19690720

# ----------------------------------- Part 1 --------------------------------- #
def intcode(ilist):
    for k in range(0, len(out := ilist.copy()), 4):
        if (opcode := out[k]) == 99: break
        elif opcode == 1: out[out[k + 3]] = out[out[k + 1]] + out[out[k + 2]]
        elif opcode == 2: out[out[k + 3]] = out[out[k + 1]] * out[out[k + 2]]

    return out

instruction_list[1:3] = 12, 2

print('Part 1: {}'.format(intcode(instruction_list)[0]))

# ----------------------------------- Part 2 --------------------------------- #
for noun, verb in product(range(100), range(0, 100, 2)):
    instruction_list[1:3] = noun, verb

    if intcode(instruction_list)[0] == goal:
        print('Part 2: {}'.format(100 * noun + verb))
        break

# ----------------------------------- Output --------------------------------- #
# Part 1: 2782414
# Part 2: 9820

# Time (mean ± σ):      54.1 ms ±   0.4 ms    [User: 51.7 ms, System: 2.5 ms]
# Range (min … max):    53.6 ms …  55.1 ms    52 runs

# ----------------------------------- Notes ---------------------------------- #
# semi-reverse engineering the input program shows the verb must be even
# in order for the output to be even
