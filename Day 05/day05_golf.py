instruction_listb = (instruction_list := [int(instruction) for instruction in open('input.txt').readline().rstrip().split(',')])[:]
def intcode(input_val, ilist: list):
    k = 0
    def decipher(s: int):
        return {'opcode': int(str(s)[-2:]), 'modes': [int(i) for i in str(s)[:-2].zfill(5)[::-1][:2] + '0']}
    def val_mode(mode: int, val: int):
        return ilist[val] if mode == 0 else val
    while True:
        if decipher(ilist[k])['opcode'] == 99: break
        elif decipher(ilist[k])['opcode'] == 1: ilist[ilist[k + 3]] = val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) + val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
        elif decipher(ilist[k])['opcode'] == 2: ilist[ilist[k + 3]] = val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) * val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2])
        elif decipher(ilist[k])['opcode'] == 3: ilist[ilist[k + 1]] = input_val
        elif decipher(ilist[k])['opcode'] == 4: print(val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]))
        elif decipher(ilist[k])['opcode'] == 5: k = val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]) if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) else k + 3
        elif decipher(ilist[k])['opcode'] == 6: k = val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]) if not val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) else k + 3
        elif decipher(ilist[k])['opcode'] == 7: ilist[ilist[k + 3]] = 1 if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) < val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]) else 0
        elif decipher(ilist[k])['opcode'] == 8: ilist[ilist[k + 3]] = 1 if val_mode(decipher(ilist[k])['modes'][0], ilist[k + 1]) == val_mode(decipher(ilist[k])['modes'][1], ilist[k + 2]) else 0
        if decipher(ilist[k])['opcode'] in [1, 2, 7, 8]: k += 4
        elif decipher(ilist[k])['opcode'] in [3, 4]: k += 2
    return ilist
intcode(1, instruction_list)
intcode(5, instruction_listb)
