""" 185 chars, 5 lines, 462 ms """
a, b = 0, 0
for i in range(147981, 691423):
    if sorted(r := list(str(i))) == r and len(set(r)) < len(r): a += 1
    if sorted(r) == r and 2 in [r.count(c) for c in r]: b += 1
print(a, b)

# """ 326 chars, 8 lines """
# def check(part):
#     rlist = []
#     for i in range(147981, 691423):
#         if sorted(a := list(str(i))) == a:
#             for pos, char in enumerate(a):
#                 if (part == 1 and len(set(a))<len(a)) or (part == a.count(char) == 2): rlist.append(i)
#     return len(set(rlist))
# print(check(1), check(2))

# if any([all([part == 1, any([char in a[0:pos], char in a[pos + 1:7]])]), part == a.count(char) == 2]): rlist.append(i)
