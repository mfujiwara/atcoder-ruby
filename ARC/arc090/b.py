import sys
from collections import defaultdict
N,M=map(int, input().split())
info=defaultdict(list)
for _ in range(M):
    l,r,d=map(int, input().split())
    info[l-1].append((r-1,d))
    info[r-1].append((l-1,-d))
rets=[None]*N
for i in range(N):
    if rets[i]!=None: continue
    rets[i]=0
    targets=[i]
    while targets:
        t=targets.pop()
        for r,d in info[t]:
            if rets[r]==None:
                rets[r]=rets[t]+d
                targets.append(r)
            else:
                if rets[r]!=rets[t]+d:
                    print("No")
                    sys.exit()
print("Yes")
