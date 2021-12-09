import collections
N=int(input())
edges=collections.defaultdict(list)
matrix=[[-1]*N for _ in range(N)]
for i in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
    matrix[a][b]=i
    matrix[b][a]=i
M=int(input())
uv=[]
for _ in range(M):
    u,v=map(int, input().split())
    uv.append((u-1,v-1))
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
paths=[0]*M
for i,uuvv in enumerate(uv):
    u,v=uuvv
    if depth[u]<depth[v]:
        u,v=v,u
    for _ in range(depth[u]-depth[v]):
        paths[i]+=pow(2,matrix[u][parent[u][0]])
        u=parent[u][0]
    while u!=v:
        paths[i]+=pow(2,matrix[u][parent[u][0]])
        paths[i]+=pow(2,matrix[v][parent[v][0]])
        u=parent[u][0]
        v=parent[v][0]
ret=pow(2,N-1)
for bit in range(1,pow(2,M)):
    total=0
    for i in range(M):
        if bit&pow(2,i)!=0:
            total|=paths[i]
    total_c=bin(total).count("1")
    if bin(bit).count("1")%2==0:
        ret+=pow(2,N-1-total_c)
    else:
        ret-=pow(2,N-1-total_c)
print(ret)
