"""161 chars, 2 lines, 0 imports, 16.4 ms"""
print(sum([(c:=lambda m:int(m)//3-2)(i)for i in[i for i in open('1')]]))
print(sum([(p:=lambda m:0if c(m)<=0else c(m)+p(c(m)))(i)for i in[i for i in open('1')]]))
