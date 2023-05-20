# ダブリング LCA：Lowest Common Ancestor
import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    x,y=map(int, input().split())
    x-=1
    y-=1
    edges[x].append(y)
    edges[y].append(x)
parent=[[] for _ in range(N)] # parent[u][k]:= u の 2^k 先の親
depth=[-1]*N
depth[0]=0
targets=[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        if depth[u]==-1:
            depth[u]=depth[t]+1
            parent[u].append(t)
            v=t
            k=0
            while len(parent[v])>k:
                parent[u].append(parent[v][k])
                v=parent[v][k]
                k+=1
            targets.append(u)
Q=int(input())
for _ in range(Q):
    a,b=map(int, input().split())
    a-=1
    b-=1
    if depth[a]<depth[b]:
        a,b=b,a
    diff=depth[a]-depth[b]
    ret=diff
    k=0
    bit=1
    while diff>0:
        if diff&bit!=0:
            a=parent[a][k]
            diff-=bit
        k+=1
        bit=bit<<1
    if a==b:
        print(ret+1)
    else:
        k=len(parent[a])-1
        for i in range(k,-1,-1):
            if len(parent[a])>i and parent[a][i]!=parent[b][i]:
                a=parent[a][i]
                b=parent[b][i]
                ret+=pow(2,i+1)
        print(ret+3)
