from itertools import permutations as perm
ils = [*map(int, open('input.txt').readline().split(','))]
phases, phases_b, signals_b = perm(range(5)), perm(range(5, 10)), []

# ----------------------------------- Part 1 --------------------------------- #
def run(phase, inp, k=0):
    it, olist = iter([phase, inp]), ils.copy()
    get = lambda m, val: val if m else olist[val]
    mode = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

    while (code := (s := olist[k]) % 100) != 99:
        if code == 1: olist[olist[k + 3]] = get(mode(s)[0], olist[k + 1]) + get(mode(s)[1], olist[k + 2])
        elif code == 2: olist[olist[k + 3]] = get(mode(s)[0], olist[k + 1]) * get(mode(s)[1], olist[k + 2])
        elif code == 3: olist[olist[k + 1]] = next(it)
        elif code == 4: return get(mode(s)[0], olist[k + 1])
        elif code == 5: k = get(mode(s)[1], olist[k + 2]) if get(mode(s)[0], olist[k + 1]) else k + 3
        elif code == 6: k = get(mode(s)[1], olist[k + 2]) if not get(mode(s)[0], olist[k + 1]) else k + 3
        elif code == 7: olist[olist[k + 3]] = 1 if get(mode(s)[0], olist[k + 1]) < get(mode(s)[1], olist[k + 2]) else 0
        elif code == 8: olist[olist[k + 3]] = 1 if get(mode(s)[0], olist[k + 1]) == get(mode(s)[1], olist[k + 2]) else 0
        k = k + 4 if code in [1, 2, 7, 8] else (k + 2 if code in [3, 4] else k)

print('Part 1: {}'.format(max([run(i[4], run(i[3], run(i[2], run(i[1], run(i[0], 0))))) for i in phases])))

# ----------------------------------- Part 2 --------------------------------- #
def icode(input_, k=0):
    it, olist = iter(input_), ils.copy()
    get = lambda m, val: val if m else olist[val]
    mode = lambda i: [*map(int, str(i)[:-2].zfill(2)[::-1][:2])]

    while (code := (s := olist[k]) % 100) != 99:
        if code == 1: olist[olist[k + 3]] = get((m := mode(s))[0], olist[k + 1]) + get(m[1], olist[k + 2])
        elif code == 2: olist[olist[k + 3]] = get((m := mode(s))[0], olist[k + 1]) * get(m[1], olist[k + 2])
        elif code == 3: olist[olist[k + 1]] = next(it)
        elif code == 4: yield get(mode(s)[0], olist[k + 1])
        elif code == 5: k = get(m[1], olist[k + 2]) if get((m := mode(s))[0], olist[k + 1]) else k + 3
        elif code == 6: k = get(m[1], olist[k + 2]) if not get((m := mode(s))[0], olist[k + 1]) else k + 3
        elif code == 7: olist[olist[k + 3]] = 1 if get((m := mode(s))[0], olist[k + 1]) < get(m[1], olist[k + 2]) else 0
        elif code == 8: olist[olist[k + 3]] = 1 if get((m := mode(s))[0], olist[k + 1]) == get(m[1], olist[k + 2]) else 0
        k = k + 4 if code in [1, 2, 7, 8] else (k + 2 if code in [3, 4] else k)

    yield 'halt'

for i in phases_b:
    amp_inp = [[i[0], 0], [i[1]], [i[2]], [i[3]], [i[4]]]
    amps = [icode(amp_inp[i]) for i in range(5)]
    while (ret := next(amps[0])) != 'halt':
        amp_inp[1].append(ret)
        for k in range(2, 5):
            amp_inp[k].append(next(amps[k - 1]))
        amp_inp[0].append(next(amps[4]))
    signals_b.append(amp_inp[0][-1])

print('Part 2: {}'.format(max(signals_b)))

# ----------------------------------- Output --------------------------------- #
# Part 1: 38834
# Part 2: 69113332

# Time (mean ± σ):      44.7 ms ±   0.7 ms    [User: 41.5 ms, System: 3.2 ms]
# Range (min … max):    44.1 ms …  47.3 ms    63 runs
