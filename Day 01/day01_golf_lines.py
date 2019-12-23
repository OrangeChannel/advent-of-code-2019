"""145 chars, 3 lines, 0 imports, 16.5 ms"""
f=[i for i in open('1')]
print(sum([(c:=lambda m:int(m)//3-2)(i)for i in f]))
print(sum([(p:=lambda m:0if c(m)<=0else c(m)+p(c(m)))(i)for i in f]))
