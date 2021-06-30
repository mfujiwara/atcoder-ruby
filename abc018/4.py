import collections
import itertools
import heapq
N,M,P,Q,R=map(int, input().split())
choco=collections.defaultdict(list)
for _ in range(R):
    x,y,z=map(int, input().split())
    x-=1
    y-=1
    choco[x].append((y,z))
ret=0
for combi in itertools.combinations([i for i in range(N)], P):
    happy=[0]*M
    for x in combi:
        for y,z in choco[x]:
            happy[y]-=z
    heapq.heapify(happy)
    h=0
    for _ in range(Q):
        z=heapq.heappop(happy)
        h-=z
    ret=max(ret,h)
print(ret)
