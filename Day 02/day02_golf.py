"""
376 chars, 15 lines, 516ms
small error on L19: if part 2 noun,verb was (12,2) again, won't print
"""
def i(l):
 k=0
 while x:=len(l):
  if l[k]==99:break
  if l[k]==1:l[l[k+3]]=l[l[k+1]]+l[l[k+2]]
  elif l[k]==2:l[l[k+3]]=l[l[k+1]]*l[l[k+2]]
  else:quit()
  k=k+4if k<=x-5else x-1
 return l[0]
from itertools import *
for o,p in product(range(100),repeat=2):
 n=[int(_)for _ in list(open('2'))[0].split(',')]
 n[1:3],g=[o,p],19690720
 if(o,p)==(12,2):print(i(n))
 elif i(n)==g:print(100*o+p)
