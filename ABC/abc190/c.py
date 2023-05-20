import itertools
from collections import defaultdict
N,M=map(int, input().split())
abs=[]
for i in range(M):
    a,b=map(int, input().split())
    abs.append((a,b))
K=int(input())
cds=[]
for i in range(K):
    c,d=map(int, input().split())
    cds.append((c,d))

ret=0
for prod in itertools.product([True, False], repeat=K):
    dict=defaultdict(int)
    for i,pr in enumerate(prod):
        c,d=cds[i]
        if pr:
            dict[c]=1
        else:
            dict[d]=1
    r=0
    for i in range(M):
        a,b=abs[i]
        if dict[a]>0 and dict[b]>0:
            r+=1
    ret=max(ret,r)
print(ret)
