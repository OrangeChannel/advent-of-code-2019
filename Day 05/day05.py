file = open('input.txt')
string_list = file.readline().rstrip().split(',')
instruction_list = [int(instruction) for instruction in string_list]
instruction_listb = instruction_list[:]


def intcode(input_val, ilist: list):
    k = 0

    def advance(current_k, distance):
        if current_k > len(ilist) - 1 - distance:  # if program isn't broken, this isn't needed
            return len(ilist) - 1
        else:
            return current_k + distance

    def decipher(s: int):
        opcode = int(str(s)[-2:])
        param_string = str(s)[:-2].zfill(5)[::-1]  # this width may have to change, I have no idea when though. This is the max amount of params any opcode can use.
        if opcode == 99:
            return {'opcode': opcode, 'modes': []}
        elif opcode == 1:  # add
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2] + '0']}
        elif opcode == 2:  # multiply
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2] + '0']}
        elif opcode == 3:  # write to param
            return {'opcode': opcode, 'modes': [0]}
        elif opcode == 4:  # read from param
            return {'opcode': opcode, 'modes': [int(param_string[0])]}
        elif opcode == 5:  # jump if true
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2]]}
        elif opcode == 6:  # jump if false
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2]]}
        elif opcode == 7:  # less than
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2] + '0']}
        elif opcode == 8:  # equals
            return {'opcode': opcode, 'modes': [int(i) for i in param_string[:2] + '0']}
        else:
            raise ValueError('opcode {} is unknown from {}'.format(opcode, s))

    def val_mode(mode: int, val: int):
        if mode == 0:  # position mode
            return ilist[val]
        elif mode == 1:  # immediate mode
            return val

    while True:
        if decipher(ilist[k])['opcode'] == 99:
            break
        elif decipher(ilist[k])['opcode'] == 1:
            calc = val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) + val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
            ilist[ilist[k + 3]] = calc
            k = advance(k, 4)
        elif decipher(ilist[k])['opcode'] == 2:
            calc = val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) * val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
            ilist[ilist[k + 3]] = calc
            k = advance(k, 4)
        elif decipher(ilist[k])['opcode'] == 3:
            ilist[ilist[k + 1]] = input_val
            k = advance(k, 2)
        elif decipher(ilist[k])['opcode'] == 4:
            print(val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]))
            k = advance(k, 2)
        elif decipher(ilist[k])['opcode'] == 5:
            if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]):
                k = val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
            else:
                k = advance(k, 3)
        elif decipher(ilist[k])['opcode'] == 6:
            if not val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]):
                k = val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
            else:
                k = advance(k, 3)
        elif decipher(ilist[k])['opcode'] == 7:
            if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) < val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]):
                ilist[ilist[k + 3]] = 1
            else:
                ilist[ilist[k + 3]] = 0
            k = advance(k, 4)
        elif decipher(ilist[k])['opcode'] == 8:
            if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) == val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]):
                ilist[ilist[k + 3]] = 1
            else:
                ilist[ilist[k + 3]] = 0
            k = advance(k, 4)
    return ilist

print('Part 1:')
intcode(1, instruction_list)

print('Part 2:')
intcode(5, instruction_listb)
