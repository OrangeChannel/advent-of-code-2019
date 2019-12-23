"""137 chars, 6 lines, 16.5 ms"""
f=open('1')
c=lambda m:int(m)//3-2
p=lambda m:0if c(m)<=0else c(m)+p(c(m))
print(sum([c(i)for i in f]))
f.seek(0)
print(sum([p(i)for i in f]))
