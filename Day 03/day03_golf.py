"""
441 chars, 11 lines
"""
a,b,c,d=open('3').readlines()[0].rstrip().split(','),open('3').readlines()[1].rstrip().split(','),{'L':-1,'R':1,'U':0,'D':0},{'L':0,'R':0,'D':-1,'U':1}
def f(l):
 p,x,y,t={},0,0,0
 for _ in l:
  for i in range(int(_[1:])):
   x+=c[_[0]]
   y+=d[_[0]]
   t+=1
   if(x,y)not in p:p[(x,y)]=t
 return p
print(min([abs(x)+abs(y)for(x,y)in set(f(a).keys())&set(f(b).keys())]),min([f(a)[i]+f(b)[i]for i in set(f(a).keys())&set(f(b).keys())]))
