import collections
import heapq
N,M=map(int, input().split())
array=list(map(int, input().split()))
h = collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    if array[u]<array[v]:
        h[u].append((v,(array[v]-array[u])*2))
        h[v].append((u,0))
    elif array[u]>array[v]:
        h[u].append((v,0))
        h[v].append((u,(array[u]-array[v])*2))
    else:
        h[u].append((v,0))
        h[v].append((u,0))
size=N
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
ret=0
for i in range(1,N):
    diff=array[0]-array[i]
    if diff<=0:
        continue
    cost=shortest[i]
    ret=max(ret,diff+cost//2-cost)
print(ret)
