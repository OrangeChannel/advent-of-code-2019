file = open('day02_input.txt')
slist = file.readlines(0)[0].rstrip().split(',')
ilist = [int(s) for s in slist]
ilist[1] = 12
ilist[2] = 2


def intcode(l: list):
    def advance(curr_k):
        if k <= len(l) - 1 - 4:
            return curr_k + 4
        else:
            return len(l) - 1

    k = 0
    while k < len(l):
        if l[k] == 99:
            break
        elif l[k] == 1:
            t = l[l[k + 1]] + l[l[k + 2]]
            l[l[k + 3]] = t
            k = advance(k)
        elif l[k] == 2:
            t = l[l[k + 1]] * l[l[k + 2]]
            l[l[k + 3]] = t
            k = advance(k)
        else:
            raise ValueError('Unknown opcode {} in pos {}'.format(l[k], k))

    return l


print('Part 1: {}'.format(intcode(ilist)[0]))

goal = 19690720
for noun in range(100):
    for verb in range(100):
        listt = [int(s) for s in slist]
        listt[1] = noun
        listt[2] = verb
        if intcode(listt)[0] == goal:
            print('Part 2: {}'.format(100*noun+verb))
