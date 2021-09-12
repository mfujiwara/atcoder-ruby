import collections
INF=-pow(10,12)
N,M=map(int, input().split())
edges=collections.defaultdict(list)
reverse=collections.defaultdict(list)
for _ in range(M):
    a,b,c=map(int, input().split())
    edges[a-1].append((b-1,c))
    reverse[b-1].append(a-1)
reachable=[False]*N
reachable[N-1]=True
targets=[N-1]
while targets:
    t=targets.pop()
    for u in reverse[t]:
        if reachable[u]: continue
        reachable[u]=True
        targets.append(u)
targets=[(0,0)] # node,score
high_scores=[INF]*N
turn=0
inf=False
while targets:
    if turn>2*N:
        inf=True
        break
    nexts=[]
    for t,score in targets:
        for u,c in edges[t]:
            new_score=score+c
            if reachable[u] and high_scores[u]<new_score:
                high_scores[u]=new_score
                nexts.append((u,new_score))
    targets=nexts
    turn+=1
if inf:
    print("inf")
else:
    print(high_scores[-1])
