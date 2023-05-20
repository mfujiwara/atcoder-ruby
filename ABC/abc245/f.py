import collections


N,M=map(int, input().split())
edges=collections.defaultdict(set)
rev_edges=collections.defaultdict(set)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].add(v)
    rev_edges[v].add(u)
targets=[]
for i in range(N):
    if len(edges[i])==0:
        targets.append(i)
while targets:
    nexts=[]
    for t in targets:
        for u in rev_edges[t]:
            edges[u].remove(t)
            if len(edges[u])==0:
                nexts.append(u)
        rev_edges[t]=set()
    targets=nexts
print(len([s for s in edges if len(edges[s])>0]))
