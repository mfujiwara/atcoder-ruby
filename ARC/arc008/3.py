import heapq
import math
N=int(input())
xytr=[]
for _ in range(N):
    x,y,t,r=map(int, input().split())
    xytr.append((x,y,t,r))
if N==1:
    print(0)
    exit()
size=N
start=0
INF=pow(10,10)
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
    x1,y1,t1,r1=xytr[u]
    for v in range(N):
        if done[v]: continue
        x2,y2,t2,r2=xytr[v]
        c=math.hypot(x1-x2,y1-y2)/min(t1,r2)
        a = shortest[u] + c
        if a < shortest[v]:
            shortest[v]=a
            heapq.heappush(queue, (a,v))
            pred[v] = u
shortest.sort(reverse=True)
shortest.pop()
ret=0
for i,a in enumerate(shortest):
    ret=max(ret,i+a)
print(ret)
