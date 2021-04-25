INF=10**8
N,M=map(int, input().split())
node_size=N-1
edges=[]
ll={}
for _ in range(M):
    u,v,l=map(int, input().split())
    if u==1:
        v-=2
        ll[v]=l
    elif v==1:
        u-=2
        ll[u]=l
    else:
        u-=2
        v-=2
        edges.append((u,v,l))
        edges.append((v,u,l))
d = [[INF]*node_size for _ in range(node_size)]
for u,v,c in edges:
    d[u][v] = c
ret=INF
for k in range(node_size):
    for i in range(node_size):
        for j in range(node_size):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if i!=j and i in ll and j in ll:
                ret=min(ret,d[i][j]+ll[i]+ll[j])
if ret<INF:
    print(ret)
else:
    print(-1)
