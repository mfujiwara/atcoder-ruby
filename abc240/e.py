import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
targets=[0]
status=[0]*N
new_index=1
rets=[None]*N
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
    else:
        status[t]=2
        min_max=None
        for u in edges[t]:
            if status[u]==2:
                if min_max==None:
                    min_max=rets[u]
                else:
                    x,y=rets[u]
                    min_max=(min(min_max[0],x),max(min_max[1],y))
        if min_max==None:
            rets[t]=(new_index,new_index)
            new_index+=1
        else:
            rets[t]=min_max
for l,r in rets:
    print(l,r)
