import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    u,v=map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
dists=[[0,0] for _ in range(N)] # nodeNum dist
done=[False]*N
done[0]=True
targets=[(0,-1)]
while targets:
    t,u=targets.pop()
    if u==-1:
        for u in edges[t]:
            if not done[u]:
                done[u]=True
                targets.append((t,u))
                targets.append((u,-1))
    else:
        dists[t][0]+=1+dists[u][0]
        dists[t][1]+=dists[u][1]+dists[u][0]+1
done=[False]*N
done[0]=True
targets=[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        if not done[u]:
            #dists[u][0]=dists[t][0]
            v1=dists[t][1]-(dists[u][1]+dists[u][0]+1)
            v0=dists[t][0]-dists[u][0]-1
            dists[u][1]+=v1+v0+1
            dists[u][0]=dists[t][0]
            done[u]=True
            targets.append(u)
for a,b in dists:
    print(b)
