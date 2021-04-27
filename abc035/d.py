from collections import defaultdict
import heapq
INF=10**11
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
N,M,T=map(int, input().split())
array=list(map(int, input().split()))
h = defaultdict(list)
h_inv = defaultdict(list)
for _ in range(M):
    a,b,c=map(int, input().split())
    h[a-1].append((b-1,c))
    h_inv[b-1].append((a-1,c))

shortest,_ = dijkstra(N, h, 0)
shortest_inv,_ = dijkstra(N, h_inv, 0)
ret=T*array[0]
for i in range(1,N):
    c=shortest[i]+shortest_inv[i]
    ret=max(ret,(T-c)*array[i])
print(ret)
