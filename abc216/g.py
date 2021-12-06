import collections
import heapq
INF=pow(10,10)
N,M=map(int, input().split())
h = collections.defaultdict(list)
for _ in range(M):
    l,r,x=map(int, input().split())
    h[l-1].append((r,r-l+1-x))
for i in range(N):
    h[i+1].append((i,0))
    h[i].append((i+1,1))

start=0
size=N+1
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
sums=[shortest[i] for i in range(N)]
rets=[0 if shortest[i+1]-shortest[i]==1 else 1 for i in range(N)]
print(*rets)
