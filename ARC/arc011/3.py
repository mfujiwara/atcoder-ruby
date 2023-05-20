from collections import defaultdict
import heapq
import sys
INF=1<<60
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
first,last=input().split()
N=int(input())
array=[input() for _ in range(N)]
if first==last:
    print(0)
    print(first)
    print(last)
    sys.exit()
array = [first] + array + [last]
edges=[]
for i in range(N+1):
    a=array[i]
    l=len(a)
    for j in range(i+1,N+2):
        b=array[j]
        if l!=len(b): continue
        c=0
        for k in range(l):
            if a[k]!=b[k]: c+=1
        if c==1:
            edges.append((i,j,1))
            edges.append((j,i,1))
shortest,pred=dijkstra(N+2,edges,0)
if shortest[N+1]==INF:
    print(-1)
else:
    print(shortest[N+1]-1)
    rets=[N+1]
    while rets[-1]!=0:
        rets.append(pred[rets[-1]])
    for r in rets[::-1]:
        print(array[r])
