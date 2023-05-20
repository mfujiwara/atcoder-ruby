import collections
import heapq
MOD=pow(10,9)+7
INF=pow(10,20)
def dijkstra(size, h, start):
    done=[False]*size
    shortest=[INF]*size
    shortest[start]=0
    pred={}
    queue=[(0, start)]
    heapq.heapify(queue)
    counts=[collections.defaultdict(int) for _ in range(size)]
    counts[start][0]=1
    while len(queue)>0:
        cost, u = heapq.heappop(queue)
        if shortest[u]<cost: continue
        done[u] = True    #探されたuは確定

        for v,c in h[u]:
            if done[v]: continue
            a = shortest[u] + c
            if a==shortest[v]:
                shortest[v]=a
                counts[v][a]+=counts[u][cost]
                counts[v][a]%=MOD
            elif a < shortest[v]:
                shortest[v]=a
                counts[v][a]+=counts[u][cost]
                counts[v][a]%=MOD
                heapq.heappush(queue, (a,v))
                pred[v] = u
    ccc=[counts[i][shortest[i]] for i in range(size)]
    return [shortest, pred,ccc]
N,M=map(int, input().split())
S,T=map(int, input().split())
S-=1
T-=1
edges=[[] for _ in range(N)]
for _ in range(M):
    u,v,d=map(int, input().split())
    u-=1
    v-=1
    edges[u].append((v,d))
    edges[v].append((u,d))
shortest1,_,counts1=dijkstra(N,edges,S)
shortest2,_,counts2=dijkstra(N,edges,T)
D=shortest1[T]
ret=pow(counts1[T],2,MOD)
for i in range(N):
    if shortest1[i]*2==D==shortest2[i]*2:
        ret-=pow(counts1[i],2,MOD)*pow(counts2[i],2,MOD)%MOD
        ret%=MOD
for i in range(N):
    for j,d in edges[i]:
        if shortest1[i]+shortest2[j]+d==D:
            if shortest1[i]*2<D<(shortest1[i]+d)*2:
                ret-=pow(counts1[i],2,MOD)*pow(counts2[j],2,MOD)%MOD
                ret%=MOD
print(ret)
# print(shortest1)
# print(shortest2)
# print(counts1)
# print(counts2)
# print(edges)