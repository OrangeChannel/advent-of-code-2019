# ----------------------------------- Part 1 --------------------------------- #
file = open('input.txt')
string_list = file.readline().split(',')
instruction_list = [*map(int, string_list)]
instruction_listb = instruction_list.copy()


def intcode(input_val, ilist: list):
    k = 0
    get = lambda mode, val: val if mode else ilist[val]

    def decipher(s: int):
        opcode = int(str(s)[-2:])
        param_string = str(s)[:-2].zfill(5)[::-1]

        return {'code': opcode, 'modes': [*map(int, param_string[:2])]}

    while True:
        s = ilist[k]
        code = decipher(s)['code']

        if code == 99:
            break

        elif code == 1:  # add
            ilist[ilist[k + 3]] = get(decipher(s)['modes'][0], ilist[k + 1]) + get(decipher(s)['modes'][1], ilist[k + 2])

        elif code == 2:  # multiply
            ilist[ilist[k + 3]] = get(decipher(s)['modes'][0], ilist[k + 1]) * get(decipher(s)['modes'][1], ilist[k + 2])

        elif code == 3:  # input
            ilist[ilist[k + 1]] = input_val

        elif code == 4:  # output
            print(get(decipher(s)['modes'][0], ilist[k + 1]))

        elif code == 5:  # jump if True
            k = get(decipher(s)['modes'][1], ilist[k + 2]) if get(decipher(s)['modes'][0], ilist[k + 1]) else k + 3

        elif code == 6:  # jump if False
            k = get(decipher(s)['modes'][1], ilist[k + 2]) if not get(decipher(s)['modes'][0], ilist[k + 1]) else k + 3

        elif code == 7:  # less than
            ilist[ilist[k + 3]] = 1 if get(decipher(s)['modes'][0], ilist[k + 1]) < get(decipher(s)['modes'][1], ilist[k + 2]) else 0

        elif code == 8:  # equals
            ilist[ilist[k + 3]] = 1 if get(decipher(s)['modes'][0], ilist[k + 1]) == get(decipher(s)['modes'][1], ilist[k + 2]) else 0

        if code in [1, 2, 7, 8]:
            k += 4
        elif code in [3, 4]:
            k += 2

    return ilist

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
