import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
targets=[0]
rets=[]
while targets:
    t=targets.pop()
    rets.append(str(t+1))
    es=sorted(edges[t])
    edges[t]=[]
    while es:
        u=es.pop()
        targets.append(t)
        targets.append(u)
        edges[u].remove(t)
print(" ".join(rets))
