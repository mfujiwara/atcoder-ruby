import collections
import heapq
N,Q=map(int, input().split())
array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
targets=[0]
status=[0]*N
children=[[] for _ in range(N)]
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
    elif status[t]==1:
        status[t]=2
        children[t]=[array[t]]
        for u in edges[t]:
            if status[u]==2:
                for s in children[u]:
                    heapq.heappush(children[t],s)
                    if len(children[t])>20:
                        heapq.heappop(children[t])
for _ in range(Q):
    v,k=map(int, input().split())
    v-=1
    children[v].sort()
    print(children[v][-k])
