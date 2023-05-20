from collections import defaultdict
import heapq
INF=1<<60
N,M,X,Y=map(int, input().split())
edges=[]
for i in range(M):
    a,b,t,k=map(int, input().split())
    edges.append((a-1,b-1,t,k))
    edges.append((b-1,a-1,t,k))

def dijkstra(size, edge_list, start):
    h = defaultdict(list)
    for u,v,t,k in edge_list:
        h[u].append((v,t,k))

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

        for v,t,k in h[u]:
            if done[v]: continue
            diff_t=0
            if shortest[u]%k!=0:
                diff_t=k-shortest[u]%k
            a = shortest[u] + diff_t + t
            if a < shortest[v]:
                shortest[v]=a
                heapq.heappush(queue, (a,v))
                pred[v] = u
    return [shortest, pred]

shortest, _ = dijkstra(N,edges,X-1)
ret=shortest[Y-1]
if ret==INF:
    print("-1")
else:
    print(ret)
