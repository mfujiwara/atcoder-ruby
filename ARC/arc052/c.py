import collections
import heapq
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    c,a,b=map(int, input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
size=N
INF=pow(10,10)
start=0

done=[collections.defaultdict(lambda: False) for _ in range(size)]
shortest=[INF]*size
shortest[start]=0
queue=[(0,0,start)]
heapq.heapify(queue)
queue2=[]

while len(queue)>0 or len(queue2)>0:
    if len(queue)==0:
        queue,queue2=queue2,queue
    # タイプBが少ない方を優先
    count,cost,u = heapq.heappop(queue)
    if shortest[u]>=cost:
        shortest[u]=cost
        done[u][count]=True
        for v,c in edges[u]:
            if c==0:
                if done[v][count]: continue
                a = shortest[u] + 1
                if a < shortest[v]:
                    heapq.heappush(queue, (count,a,v))
            else:
                # タイプBが増える場合は別queue
                a = shortest[u] + count+1
                if a < shortest[v]:
                    heapq.heappush(queue2, (count+1,a,v))
for i in range(N):
    print(shortest[i])
