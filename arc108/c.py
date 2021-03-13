from collections import defaultdict
N,M=map(int, input().split())
edges=defaultdict(list)
for _ in range(M):
    u,v,c=map(int, input().split())
    edges[u-1].append((v-1,c))
    edges[v-1].append((u-1,c))
rets=[-1]*N
targets=[0] # (id, parent_id, parent_edge)
rets[0]=1
while targets:
    t=targets.pop()
    t_c=rets[t]
    for v,c in edges[t]:
        if rets[v]!=-1: continue
        if t_c==c:
            rets[v]= 1 if c!=1 else 2
        else:
            rets[v]=c
        targets.append(v)
for r in rets:
    print(r)
