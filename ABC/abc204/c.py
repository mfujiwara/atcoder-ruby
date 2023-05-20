from collections import defaultdict
import heapq
INF=1<<60
def dijkstra(size, h, start):
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
    return [shortest, pred]

N,M=map(int, input().split())
h = defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    h[a-1].append((b-1,1))
for i in range(N):
    h[i].append((i,0))
ret=0
for i in range(N):
    d,_=dijkstra(N,h,i)
    unreacheable=d.count(INF)
    ret+=(N-unreacheable)
print(ret)
