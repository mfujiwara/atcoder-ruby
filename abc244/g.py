import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
S=list(map(int,list(input())))
done=[False]*N
done[0]=True
targets=[(0,-1,0)]
tree_edges=collections.defaultdict(list)
rets=[]
while targets:
    t,p,status=targets.pop()
    if status==0:
        rets.append(t)
        S[t]^=1
        targets.append((t,p,2))        
        for u in edges[t]:
            if done[u]: continue
            done[u]=True
            tree_edges[t].append(u)
            targets.append((u,t,1))
            targets.append((u,t,0))
    elif status==1:
        rets.append(p)
        S[p]^=1
    else:
        for u in tree_edges[t]:
            if S[u]==1:
                rets.append(u)
                S[u]^=1
                rets.append(t)
                S[t]^=1
if S[0]==1:
    u=tree_edges[0][0]
    rets.append(u)
    rets.append(t)
    rets.append(u)
print(len(rets))
print(*list(map(lambda e:e+1,rets)))
