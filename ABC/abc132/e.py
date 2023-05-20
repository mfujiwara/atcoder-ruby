from collections import defaultdict
import heapq
INF=10**10
N,M=map(int, input().split())
h=defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    h[u-1].append((N+v-1,1))
    h[N+u-1].append((2*N+v-1,1))
    h[2*N+u-1].append((v-1,1))
S,T=map(int, input().split())

start=S-1
size=N*3
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

if shortest[T-1]==INF:
    print(-1)
else:
    print(shortest[T-1]//3)
