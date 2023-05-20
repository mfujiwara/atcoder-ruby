import sys
from collections import defaultdict
import heapq
INF=10**10
R,C=map(int, input().split())
size=R*C*2
start=0
h = defaultdict(list)
for i in range(R):
    array=list(map(int, input().split()))
    base=i*C
    for j,a in enumerate(array):
        node=base+j
        h[node].append((node+1,a))
        h[node+1].append((node,a))
for i in range(R-1):
    array=list(map(int, input().split()))
    base=i*C
    for j,a in enumerate(array):
        node=base+j
        h[node].append((node+C,a))
        t=node+R*C
        h[t].append((node,1))
        h[node+C].append((t+C,0))
        h[t+C].append((t,1))
done=[False]*size
shortest=[INF]*size
shortest[start]=0
pred={}
queue=[(0, start)]
heapq.heapify(queue)

while len(queue)>0:
    cost, u = heapq.heappop(queue)
    if shortest[u]<cost: continue
    done[u] = True    #探されたuは確定

    for v,c in h[u]:
        if done[v]: continue
        a = shortest[u] + c
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
print(shortest[-1])
