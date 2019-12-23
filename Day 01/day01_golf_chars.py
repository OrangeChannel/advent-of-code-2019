"""
170 chars, 9 lines, 0 imports, 16.3 ms
f: input file
a: anon fuel function
s: starts at 0
"""
f=open('1')
a,s=lambda i:int(i)//3-2,0
print((sum([a(i)for i in f])))
f.seek(0)
for i in f:
    if(x:=a(i))>0:
        s+=x
        while a(x)>0:
            s+=(x:=a(x))
print(s)
