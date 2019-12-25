for (input_val, ilist) in [(1, [int(instruction) for instruction in open('input.txt').readline().rstrip().split(',')])[:], (5, [int(instruction) for instruction in open('input.txt').readline().rstrip().split(',')])[:]]:
    k = 0
    while True:
        if (a:=int(str(ilist[k])[-2:])) == 99: break
        elif a == 1: ilist[ilist[k + 3]] = (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) + (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2])
        elif a == 2: ilist[ilist[k + 3]] = (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) * (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2])
        elif a == 3: ilist[ilist[k + 1]] = input_val
        elif a == 4: print(ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1])
        elif a == 5: k = (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2]) if (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) else k + 3
        elif a == 6: k = (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2]) if not (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) else k + 3
        elif a == 7: ilist[ilist[k + 3]] = 1 if (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) < (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2]) else 0
        elif a == 8: ilist[ilist[k + 3]] = 1 if (ilist[ilist[k + 1]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else ilist[k + 1]) == (ilist[ilist[k + 2]] if [int(i) for i in str(ilist[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else ilist[k + 2]) else 0
        k = k + 4 if a in [1,2,7,8] else (k + 2 if a in [3,4] else k)
