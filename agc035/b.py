import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
if M%2==1:
    print(-1)
    exit()
status=[0]*N
targets=[0]
status[0]=1
parents=[-1]*N
rets=collections.defaultdict(list)
while targets:
    t=targets.pop()
    if status[t]==1:
        status[t]=2
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                status[u]=1
                targets.append(u)
                parents[u]=t
    else:
        status[t]=3
        parent=parents[t]
        if parent==-1:
            continue
        for u in edges[t]:
            if status[u]==3:
                continue
            if parents[t]!=u:
                rets[t].append(u)
        
        if parent>=0:
            if len(rets[t])%2==0:
                rets[parent].append(t)
            else:
                rets[t].append(parent)
for a in rets:
    for b in rets[a]:
        print(a+1,b+1)
