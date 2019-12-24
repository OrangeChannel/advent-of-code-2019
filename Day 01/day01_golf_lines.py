"""154 chars, 1 lines, 0 imports, 16.4 ms"""
print(sum([(c:=lambda m:int(m)//3-2)(i)for i in[i for i in open('1')]]),sum([(p:=lambda m:c(m)+p(c(m))if c(m)>0else 0)(i)for i in[i for i in open('1')]]))
