from collections import defaultdict
import heapq
INF=10**6
def dijkstra(size, edge_list, start):
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
N,M=map(int, input().split())
mat=[[False]*N for _ in range(N)]
edges=[]
for _ in range(M):
    a,b,c=map(int, input().split())
    edges.append((a-1,b-1,c))
    edges.append((b-1,a-1,c))
    mat[a-1][b-1]=True
    mat[b-1][a-1]=True
for i in range(N):
    shortest, pred = dijkstra(N, edges, i)
    for key in pred:
        value=pred[key]
        mat[key][value]=False
        mat[value][key]=False
ret=0
for i in range(N):
    for j in range(N):
        if mat[i][j]: ret+=1
print((ret//2))
