import collections
import heapq
N,Q=map(int, input().split())
h=collections.defaultdict(list)
for _ in range(Q):
    l,r=map(int, input().split())
    l-=1
    h[l].append((r,1))
    h[r].append((l,1))

size=N+1
INF=pow(10,10)
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

    for v,c in h[u]:
        if done[v]: continue
        a = shortest[u] + c
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
if shortest[N]==INF:
    print("No")
else:
    print("Yes")
