import collections
import heapq
INF=pow(10,15)
N,M,S=map(int, input().split())
h = collections.defaultdict(list)
for _ in range(M):
    u,v,a,b=map(int, input().split())
    u-=1
    v-=1
    for i in range(2500-a):
        h[u*2500+i+a].append((v*2500+i,b))
        h[v*2500+i+a].append((u*2500+i,b))
for i in range(N):
    c,d=map(int, input().split())
    for j in range(2500-c):
        h[i*2500+j].append((i*2500+j+c,d))
size=N*2500 # node,silver=divmod(i,2500)
start=min(2499,S)
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
ret=[INF]*N
for i,c in enumerate(shortest):
    ret[i//2500]=min(ret[i//2500],c)
for i in range(1,N):
    print(ret[i])
