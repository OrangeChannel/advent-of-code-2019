"""
329 chars, 8 lines, 2 imports, 17.0 ms
"""
import math, fileinput
fuel, start = lambda i: math.floor(int(i) / 3) - 2, 0
print('Part 1: {}'.format(sum([fuel(i) for i in fileinput.input('day01_input.txt')])))
for i in fileinput.input('1'):
    if (x := fuel(i)) > 0:
        start += x
        while fuel(x) > 0:
            start += (x := fuel(x))
print('Part 2: {}'.format(start))
