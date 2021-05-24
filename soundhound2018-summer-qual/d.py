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

n,m,s,t=map(int, input().split())
hs=defaultdict(list)
ht=defaultdict(list)
for _ in range(m):
    u,v,a,b=map(int, input().split())
    hs[u-1].append((v-1,a))
    hs[v-1].append((u-1,a))
    ht[u-1].append((v-1,b))
    ht[v-1].append((u-1,b))
shortest_s,_=dijkstra(n,hs,s-1)
shortest_t,_=dijkstra(n,ht,t-1)
costs=[shortest_s[i]+shortest_t[i] for i in range(n)]
for i in range(n-2,-1,-1):
    costs[i]=min(costs[i],costs[i+1])
for i in range(n):
    print(10**15-costs[i])
