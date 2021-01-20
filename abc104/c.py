import itertools
D,G=list(map(int, input().split()))
G/=100
qs=[]
for i in range(D):
    p,c=list(map(int, input().split()))
    qs.append([(i+1), p, (i+1)*p+c/100])
ret=10**10
for prod in itertools.product([True, False], repeat=D):
    r=0
    sum=0
    taseru=None
    for i,pr in enumerate(prod):
        if pr:
            sum+=qs[i][2]
            r+=qs[i][1]
        else:
            taseru=qs[i]
    if sum>=G:
        if ret>r:
            ret=r
        continue
    if taseru != None:
        i,p,pp=taseru
        n=int((G-sum+i-1)/i)
        if n<p:
            r+=n
            if ret>r:
                ret=r
print(ret)
