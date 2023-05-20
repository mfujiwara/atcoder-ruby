from collections import defaultdict
import heapq
INF=1<<100
def dijkstra_oni(size, edge_list, start):
    h = defaultdict(list)
    for u,v,c in edge_list:
        h[u].append((v,c))

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

N,U,V=map(int, input().split())
U-=1
V-=1
edges=[]
for _ in range(N-1):
    a,b=map(int, input().split())
    edges.append((a-1,b-1,1))
    edges.append((b-1,a-1,1))
d_oni,d_pred=dijkstra_oni(N,edges,V)
def dijkstra(size, edge_list, start, d_oni):
    max_d=d_oni[start]
    max_v=start
    h = defaultdict(list)
    for u,v,c in edge_list:
        h[u].append((v,c))

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
            if a < shortest[v] and a<=d_oni[v]:
                shortest[v]=a                
                heapq.heappush(queue, (a,v))
                pred[v] = u
                if d_oni[v]>max_d:
                    max_d=d_oni[v]
                    max_v=v
    return [shortest, pred, max_v]

_,_,max_v=dijkstra(N,edges,U, d_oni)
print(max(0,d_oni[max_v]-1))
