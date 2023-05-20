import heapq
N,M=map(int, input().split())
children=[set() for _ in range(N)]
parents=[set() for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    children[a].add(b)
    parents[b].add(a)
no_parents=[]
for i in range(N):
    if len(parents[i])==0:
        no_parents.append(i)
heapq.heapify(no_parents)
rets=[]
while no_parents:
    t=heapq.heappop(no_parents)
    rets.append(t)
    for u in children[t]:
        parents[u].remove(t)
        if len(parents[u])==0:
            heapq.heappush(no_parents,u)
if len(rets)==N:
    print(*[r+1 for r in rets])
else:
    print(-1)
