import sys
import itertools
N=int(input())
array=list(map(int, input().split()))
if N==1:
    print(array[0])
    sys.exit()
ors=[[-1]*N for _ in range(N)]
for i in range(N):
    ors[i][i]=array[i]
    for j in range(i+1,N):
        ors[i][j]=ors[i][j-1] | array[j]
rets=[]
for prod in itertools.product([True,False],repeat=N-1):
    counts=[1]
    for p in prod:
        if p:
            counts[-1]+=1
        else:
            counts.append(1)
    base=0
    ooo=[]
    for c in counts:
        ooo.append(ors[base][base+c-1])
        base+=c
    if len(ooo)==1:
        rets.append(ooo[0])
    else:
        r=0
        for o in ooo:
            r^=o
        rets.append(r)
print(min(rets))
