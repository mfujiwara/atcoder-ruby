import heapq
import collections
a,N=map(int, input().split())
done=set()
shortest={}
shortest[N]=0
queue=[(0, N)]
heapq.heapify(queue)

while len(queue)>0:
    cost, u = heapq.heappop(queue)
    if shortest[u]<cost: continue
    done.add(u)

    nexts=[]
    ustr=str(u)
    if len(ustr)>1 and ustr[1]!="0":
        nexts.append(int(ustr[1:]+ustr[0]))
    if u%a==0:
        nexts.append(u//a)
    for v in nexts:
        if v in done: continue
        aa = shortest[u] + 1
        if v not in shortest or aa < shortest[v]:
            shortest[v]=aa
            heapq.heappush(queue, (aa,v))
if 1 not in shortest:
    print(-1)
else:
    print(shortest[1])
