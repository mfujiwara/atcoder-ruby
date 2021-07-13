N,M,D=map(int, input().split())
array=list(map(int, input().split()))
one=[i for i in range(N)]
for a in array:
    one[a],one[a-1]=one[a-1],one[a]
targets=set([i for i in range(N)])
rets=[-1]*N
while targets:
    t=targets.pop()
    loop=[t]
    u=one[t]
    while u!=t:
        targets.remove(u)
        loop.append(u)
        u=one[u]
    d=D%len(loop)
    if d!=0:
        d=len(loop)-d
    for i,l in enumerate(loop):
        rets[l]=loop[(i+d)%len(loop)]
for r in rets:
    print(r+1)
