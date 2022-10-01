import heapq
N,M,src,dst=map(int, input().split())
# edges[i]:=(a,b,c,d)|aからiまでのコストb,aから終点cについてしまった時のコストd
edges=[[] for _ in range(N)]
for _ in range(M):
    l=int(input())
    s_array=list(map(int, input().split()))
    w_array=list(map(int, input().split()))
    total=0
    for i in range(l-1):
        s=s_array[i]
        t=s_array[i+1]
        c=w_array[i]
        total+=c
        edges[s].append((t,c,s_array[0],total))
    for i in range(l-1):
        s=s_array[i]
        t=s_array[i+1]
        c=w_array[i]
        edges[t].append((s,c,s_array[-1],total))
        total-=c
INF=pow(10,20)
start=dst
size=len(edges)
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

    for v,c,_,_ in edges[u]:
        if done[v]: continue
        a = shortest[u] + c
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
shortest2=shortest.copy()

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

    for v,c,v2,c2 in edges[u]:
        if done[v]: continue
        a = max(shortest[u]+c, shortest2[v2]+c2)
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
print(shortest[src])
# print(shortest)
# print(shortest2)
# print(edges)
