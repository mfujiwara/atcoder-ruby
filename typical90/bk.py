import collections
H,W=map(int, input().split())
P=[list(map(int, input().split())) for _ in range(H)]
ret=0
for i in range(1,pow(2,H)):
    hs=[]
    k=0
    while i>0:
        i,r=divmod(i,2)
        if r==1:
            hs.append(k)
        k+=1
    array=P[hs[0]][:]
    for h in range(1,len(hs)):
        for j,a in enumerate(P[hs[h]]):
            if a!=array[j]:
                array[j]=0
    counts=collections.defaultdict(int)
    for a in array:
        if a!=0:
            counts[a]+=1
    c_max=0
    for c in counts:
        c_max=max(c_max,counts[c])
    ret=max(ret,c_max*len(hs))
print(ret)
