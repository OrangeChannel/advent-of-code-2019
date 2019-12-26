# ----------------------------------- Part 1 --------------------------------- #
start, end = 147981, 691423
part1, part2 = 0, 0

for i in range(start + 18, end - 1423):
    if i % 10 > 1:  # if ends in a zero or 1 don't include
        chars = list(str(i))
        if sorted(chars) == chars:
            if len(set(chars)) < len(chars):
                part1 += 1
            if 2 in [chars.count(number) for number in chars]:
                part2 += 1

print('Part 1: {}'.format(part1))

# ----------------------------------- Part 2 --------------------------------- #
print('Part 2: {}'.format(part2))

# ----------------------------------- Output --------------------------------- #
# Part 1: 1790
# Part 2: 1206

# ----------------------------------- Notes --------------------------------- #
# numbers 147981..147998 not included because numbers after 9 must all be 9's
# numbers 690000..691423 not included because ''
# by checking if number ends in a zero or a 1 we achieve 11% speedup
#   because the lowest valid number that ends in a 1 is 111111 and is less than
#   our starting point
# `if i % 10 not in [0,1]` is 1% slower
