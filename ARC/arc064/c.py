import collections
import heapq
xs,ys,xt,yt=map(int, input().split())
N=int(input())
discs=[(xs,ys,0)]
for _ in range(N):
    x,y,r=map(int, input().split())
    discs.append((x,y,r))
discs.append((xt,yt,0))
h=collections.defaultdict(list)
for i in range(N+1):
    xi,yi,ri=discs[i]
    for j in range(i+1,N+2):
        xj,yj,rj=discs[j]
        d=pow((xi-xj)**2+(yi-yj)**2,0.5)
        d=max(d-ri-rj,0)
        h[i].append((j,d))
        h[j].append((i,d))
INF=h[0][-1][1]
size=N+2
start=0
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
ret=shortest[N+1]
print(ret)
