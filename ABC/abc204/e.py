import math
from collections import defaultdict
import heapq
INF=1<<60
N,M=map(int, input().split())
h = defaultdict(list)
for _ in range(M):
    a,b,c,d=map(int, input().split())
    h[a-1].append((b-1,c,d))
    h[b-1].append((a-1,c,d))

size=N
start=0
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

    for v,c,d in h[u]:
        if done[v]: continue
        x=max(0,pow(d,0.5)-shortest[u]-1)
        x1=math.ceil(x)
        x0=x1+1
        x2=math.floor(x)
        x3=max(0,x2-1)
        dx=min(x0+d//(x0+shortest[u]+1),x1+d//(x1+shortest[u]+1),x2+d//(x2+shortest[u]+1),x3+d//(x3+shortest[u]+1))
        a = shortest[u] + c + dx
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
if shortest[N-1]!=INF:
    print(shortest[N-1])
else:
    print(-1)
