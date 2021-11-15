import collections
import heapq
N,L=map(int, input().split())
h = collections.defaultdict(list)
for _ in range(N):
    l,r,c=map(int, input().split())
    h[l].append((r,c))
for i in range(L):
    h[i+1].append((i,0))
size=L+1
INF=pow(10,11)
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
print(shortest[-1])
