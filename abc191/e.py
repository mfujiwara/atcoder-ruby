from collections import defaultdict
import heapq
INF=10**10
N,M=map(int, input().split())
self_short=[INF]*N
edge_list=defaultdict(list)
for i in range(M):
    a,b,c=map(int, input().split())
    if a==b:
        self_short[a-1]=min(self_short[a-1],c)
    else:
        edge_list[a-1].append((b-1,c))

def dijkstra(size, start):
    done=[False]*N
    shortest=[INF]*N
    shortest[start]=0
    pred={}
    queue=[(0, start)]
    heapq.heapify(queue)

    while len(queue)>0:
        cost, u = heapq.heappop(queue)
        if shortest[u]<cost: continue
        done[u] = True    #探されたuは確定

        for v,c in edge_list[u]:
            if done[v]: continue
            a = shortest[u] + c
            if a < shortest[v]:
                shortest[v]=a
                heapq.heappush(queue, (a,v))
                pred[v] = u
    return [shortest, pred]

shortests=[dijkstra(N,i)[0] for i in range(N)]
for i in range(N):
    ret=self_short[i]
    for j in range(N):
        if i==j: continue
        ret=min(ret,shortests[i][j]+shortests[j][i])
    print(ret if ret<INF else "-1")
