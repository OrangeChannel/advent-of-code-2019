from itertools import permutations
instruction_list = [*map(int, open('input.txt').readline().split(','))]
phases, signals = permutations(range(5)), []

# ----------------------------------- Part 1 --------------------------------- #
class Amplifier:

    def __init__(self, phase, inp, olist):
        self.phase = phase
        self.inp = inp
        self.olist = olist

    def intcode(self, k=0):
        it = iter([self.phase, self.inp])
        L = self.olist.copy()
        g = lambda mode, val: val if mode else L[val]
        m = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

        while (code := (s := L[k]) % 100) != 99:
            if code == 1:  # add
                L[L[k + 3]] = g(m(s)[0], L[k + 1]) + g(m(s)[1], L[k + 2])
            elif code == 2:  # multiply
                L[L[k + 3]] = g(m(s)[0], L[k + 1]) * g(m(s)[1], L[k + 2])
            elif code == 3:  # input
                L[L[k + 1]] = next(it, 0)
            elif code == 4:  # output
                return g(m(s)[0], L[k + 1])
            elif code == 5:  # jump if True
                k = g(m(s)[1], L[k + 2]) if g(m(s)[0], L[k + 1]) else k + 3
            elif code == 6:  # jump if False
                k = g(m(s)[1], L[k + 2]) if not g(m(s)[0], L[k + 1]) else k + 3
            elif code == 7:  # less than
                L[L[k + 3]] = 1 if g(m(s)[0], L[k + 1]) < g(m(s)[1], L[k + 2]) else 0
            elif code == 8:  # equals
                L[L[k + 3]] = 1 if g(m(s)[0], L[k + 1]) == g(m(s)[1], L[k + 2]) else 0

            if code in [1, 2, 7, 8]: k += 4
            elif code in [3, 4]: k += 2

for i in phases:
    A = Amplifier(i[0], 0, instruction_list)
    B = Amplifier(i[1], A.intcode(), instruction_list)
    C = Amplifier(i[2], B.intcode(), instruction_list)
    D = Amplifier(i[3], C.intcode(), instruction_list)
    E = Amplifier(i[4], D.intcode(), instruction_list)
    signals.append(E.intcode())

print('Part 1: {}'.format(max(signals)))

# ----------------------------------- Part 2 --------------------------------- #
# FeelsDumbMan

# ----------------------------------- Output --------------------------------- #
# Part 1: 38834

# Time (mean ± σ):      24.7 ms ±   0.3 ms    [User: 21.3 ms, System: 3.3 ms]
# Range (min … max):    24.3 ms …  26.2 ms    108 runs
