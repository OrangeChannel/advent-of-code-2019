string_list = open('input.txt').readline().split(',')
instruction_listb = (instruction_list := [*map(int, string_list)]).copy()

# ----------------------------------- Part 1 --------------------------------- #
def intcode(input_val, ilist, k=0):
    get = lambda mode, val: val if mode else ilist[val]
    modes = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

    while (code := (s := ilist[k]) % 100) != 99:
        if code == 1:  # add
            ilist[ilist[k + 3]] = get((m := modes(s))[0], ilist[k + 1]) + \
                                  get(m[1], ilist[k + 2])
        elif code == 2:  # multiply
            ilist[ilist[k + 3]] = get((m := modes(s))[0], ilist[k + 1]) * \
                                  get(m[1], ilist[k + 2])
        elif code == 3:  # input
            ilist[ilist[k + 1]] = input_val
        elif code == 4:  # output
            print(get(modes(s)[0], ilist[k + 1]))
        elif code == 5:  # jump if True
            k = get(m[1], ilist[k + 2]) if \
                get((m := modes(s))[0], ilist[k + 1]) else k + 3
        elif code == 6:  # jump if False
            k = get(m[1], ilist[k + 2]) if not \
                get((m := modes(s))[0], ilist[k + 1]) else k + 3
        elif code == 7:  # less than
            ilist[ilist[k + 3]] = 1 if get((m := modes(s))[0], ilist[k + 1]) < \
                                       get(m[1], ilist[k + 2]) else 0
        elif code == 8:  # equals
            ilist[ilist[k + 3]] = 1 if get((m := modes(s))[0], ilist[k + 1]) == \
                                       get(m[1], ilist[k + 2]) else 0

        if code in [1, 2, 7, 8]: k += 4
        elif code in [3, 4]: k += 2

print('Part 1:')
intcode(1, instruction_list)

# ----------------------------------- Part 2 --------------------------------- #
print('\nPart 2:')
intcode(5, instruction_listb)

# ----------------------------------- Output --------------------------------- #
# Part 1:
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 13787043
#
# Part 2:
# 3892695

# Time (mean ± σ):      16.4 ms ±   0.2 ms    [User: 13.7 ms, System: 2.8 ms]
# Range (min … max):    16.2 ms …  17.3 ms    157 runs
