for (v, l) in [(1, [int(i) for i in open('input.txt').readline().rstrip().split(',')])[:], (5, [int(i) for i in open('input.txt').readline().rstrip().split(',')])[:]]:
    k = 0
    while True:
        if (a:=int(str(l[k])[-2:])) == 99: break
        elif a == 1: l[l[k + 3]] = (l[l[k + 1]] if (o:=[int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'])[0] == 0 else l[k + 1]) + (l[l[k + 2]] if o[1] == 0 else l[k + 2])
        elif a == 2: l[l[k + 3]] = (l[l[k + 1]] if (o:=[int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'])[0] == 0 else l[k + 1]) * (l[l[k + 2]] if o[1] == 0 else l[k + 2])
        elif a == 3: l[l[k + 1]] = v
        elif a == 4: print(l[l[k + 1]] if [int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else l[k + 1])
        elif a == 5: k = (l[l[k + 2]] if [int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else l[k + 2]) if (l[l[k + 1]] if [int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else l[k + 1]) else k + 3
        elif a == 6: k = (l[l[k + 2]] if [int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'][1] == 0 else l[k + 2]) if not (l[l[k + 1]] if [int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'][0] == 0 else l[k + 1]) else k + 3
        elif a == 7: l[l[k + 3]] = 1 if (l[l[k + 1]] if (o:=[int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'])[0] == 0 else l[k + 1]) < (l[l[k + 2]] if o[1] == 0 else l[k + 2]) else 0
        elif a == 8: l[l[k + 3]] = 1 if (l[l[k + 1]] if (o:=[int(i) for i in str(l[k])[:-2].zfill(5)[::-1][:2] + '0'])[0] == 0 else l[k + 1]) == (l[l[k + 2]] if o[1] == 0 else l[k + 2]) else 0
        k = k + 4 if a in [1,2,7,8] else (k + 2 if a in [3,4] else k)

# For learning purposes, taken from https://www.reddit.com/user/u794575248/
I = open('input.txt').readline().rstrip()
def R(I,X,e=__import__('operator'),S=list.__setitem__):
    def J(t,a):nonlocal i;i=a if t else i
    W=0,4,4,2,2,3,3,4,4;T=lambda f:lambda a,b,c:S(p,c,f(a,b));i,p=0,[*map(int,I.split(','))]
    F=0,T(e.add),T(e.mul),lambda a:S(p,a,X),print,J,lambda a,b:J(a==0,b),T(e.lt),T(e.eq)
    D=lambda v:(c:=v%10,w:=W[c],[v//10**j&1|(398&2**c>0)&(j==w)for j in range(2,w+1)])
    while p[i]!=99:t=i;c,w,M=D(p[i]);F[c](*[x if m else p[x]for m,x in zip(M,p[i+1:])]);J(t==i,t+w)
R(I,1),R(I,5)

