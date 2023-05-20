import collections
N=int(input())
edges=collections.defaultdict(dict)
for _ in range(N-1):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    edges[a][b]=c
    edges[b][a]=c
array=list(map(int, input().split()))
dp_d=[[] for _ in range(N)]
dp_u=[-1]*N
parents=[-1]*N
targets=[(0,True)]
while targets:
    t,first=targets.pop()
    if len(edges[t])==0:
        dp_d[t].append((0,-1))
    elif not first:
        vals=[]
        for u in edges[t]:
            v=max([dp_d[u][0][0]+edges[t][u],edges[t][u]+array[u]])
            vals.append((v,u))
        if len(vals)==1:
            dp_d[t]=vals
        else:
            max_val=max(vals)
            dp_d[t].append(max_val)
            vals.remove(max_val)
            dp_d[t].append(max(vals))
    else:
        targets.append((t,False))
        for u in edges[t]:
            edges[u].pop(t)
            parents[u]=t
            targets.append((u,True))
targets=[0]
while targets:
    t=targets.pop()
    keys=list(edges[t].keys())
    if len(keys)==0:
        continue
    elif len(keys)==1:
        u=keys[0]
        dp_u[u]=edges[t][u]+max(array[t],dp_u[t])
    else:
        for u in keys:
            if dp_d[t][0][1]==u:
                max_dpd=dp_d[t][1][0]
            else:
                max_dpd=dp_d[t][0][0]
            dp_u[u]=edges[t][u]+max([max_dpd,array[t],dp_u[t]])
    for u in keys:
        targets.append(u)
for i in range(N):
    ret=max(dp_d[i][0][0],dp_u[i])
    print(ret)
