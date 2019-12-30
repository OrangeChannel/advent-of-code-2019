from itertools import permutations
instruction_list = [*map(int, open('input.txt').readline().split(','))]
phases, phases_b, signals, signals_b = permutations(range(5)), permutations(range(5, 10)),[],[]

# ----------------------------------- Part 1 --------------------------------- #
class Amplifier:

    def __init__(self, phase, inp, ilist):
        self.phase = phase
        self.inp = inp
        self.ilist = ilist

    def intcode(self, k=0):
        it = iter([self.phase, self.inp])
        olist = self.ilist.copy()
        get = lambda mode, val: val if mode else olist[val]
        mode = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

        while (code := (s := olist[k]) % 100) != 99:
            if code == 1:  # add
                olist[olist[k + 3]] = get(mode(s)[0], olist[k + 1]) + get(mode(s)[1], olist[k + 2])
            elif code == 2:  # multiply
                olist[olist[k + 3]] = get(mode(s)[0], olist[k + 1]) * get(mode(s)[1], olist[k + 2])
            elif code == 3:  # input
                olist[olist[k + 1]] = next(it, 0)
            elif code == 4:  # output
                return get(mode(s)[0], olist[k + 1])
            elif code == 5:  # jump if True
                k = get(mode(s)[1], olist[k + 2]) if get(mode(s)[0], olist[k + 1]) else k + 3
            elif code == 6:  # jump if False
                k = get(mode(s)[1], olist[k + 2]) if not get(mode(s)[0], olist[k + 1]) else k + 3
            elif code == 7:  # less than
                olist[olist[k + 3]] = 1 if get(mode(s)[0], olist[k + 1]) < get(mode(s)[1], olist[k + 2]) else 0
            elif code == 8:  # equals
                olist[olist[k + 3]] = 1 if get(mode(s)[0], olist[k + 1]) == get(mode(s)[1], olist[k + 2]) else 0

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
class Amplifier:

    def __init__(self, phase, input_, ilist, called: bool=False):
        self.phase = phase
        self.input_ = input_
        self.ilist = ilist
        self.called = called

    def intcode(self, k=0):
        it = iter([self.phase, self.input_])
        olist = self.ilist.copy()
        get = lambda mode, val: val if mode else olist[val]
        mode = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

        while (code := (s := olist[k]) % 100) != 99:
            if code == 1:  # add
                olist[olist[k + 3]] = get((m := mode(s))[0], olist[k + 1]) + get(m[1], olist[k + 2])
            elif code == 2:  # multiply
                olist[olist[k + 3]] = get((m := mode(s))[0], olist[k + 1]) * get(m[1], olist[k + 2])
            elif code == 3:  # input
                olist[olist[k + 1]] = next(it) if not self.called else self.input_
            elif code == 4:  # output
                yield (get(mode(s)[0], olist[k + 1]), olist, k + 2)
            elif code == 5:  # jump if True
                k = get(m[1], olist[k + 2]) if get((m := mode(s))[0], olist[k + 1]) else k + 3
            elif code == 6:  # jump if False
                k = get(m[1], olist[k + 2]) if not get((m := mode(s))[0], olist[k + 1]) else k + 3
            elif code == 7:  # less than
                olist[olist[k + 3]] = 1 if get((m := mode(s))[0], olist[k + 1]) < get(m[1], olist[k + 2]) else 0
            elif code == 8:  # equals
                olist[olist[k + 3]] = 1 if get((m := mode(s))[0], olist[k + 1]) == get(m[1], olist[k + 2]) else 0

            if code in [1, 2, 7, 8]: k += 4
            elif code in [3, 4]: k += 2

        yield 'halt'

for phase in phases_b:
    called = False
    Ak, Bk, Ck, Dk, Ek = [0] * 5
    Ey = [0] * 3
    alist, blist, clist, dlist, elist = [instruction_list] * 5
    while True:
        A = Amplifier(phase[0], Ey[0], alist, called)
        Ay = next(A.intcode(Ak))
        if Ay == 'halt': break
        alist, Ak = Ay[1:3]

        B = Amplifier(phase[1], Ay[0], blist, called)
        By = next(B.intcode(Bk))
        blist, Bk = By[1:3]

        C = Amplifier(phase[2], By[0], clist, called)
        Cy = next(C.intcode(Ck))
        clist, Ck = Cy[1:3]

        D = Amplifier(phase[3], Cy[0], dlist, called)
        Dy = next(D.intcode(Dk))
        dlist, Dk = Dy[1:3]

        E = Amplifier(phase[4], Dy[0], elist, called)
        Ey = next(E.intcode(Ek))
        elist, Ek = Ey[1:3]

        called = True
    signals_b.append(Ey[0])

print('Part 2: {}'.format(max(signals_b)))

# ----------------------------------- Output --------------------------------- #
# Part 1: 38834
# Part 2: 69113332

# Time (mean ± σ):      56.7 ms ±   0.4 ms    [User: 54.3 ms, System: 2.5 ms]
# Range (min … max):    56.1 ms …  58.2 ms    50 runs
