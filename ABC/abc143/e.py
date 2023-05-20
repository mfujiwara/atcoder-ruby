INF=1<<60
N,M,L=map(int, input().split())
node_size=N
d = [[INF]*node_size for _ in range(node_size)]
for _ in range(M):
    a,b,c=map(int, input().split())
    if c>L:
        continue
    a-=1
    b-=1
    d[a][b]=c
    d[b][a]=c
for i in range(N):
    d[i][i]=0
for k in range(node_size):
    for i in range(node_size):
        for j in range(node_size):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
d2=[[INF]*node_size for _ in range(node_size)]
for i in range(N):
    for j in range(i,N):
        if d[i][j]<=L:
            d2[i][j]=1
            d2[j][i]=1
for k in range(node_size):
    for i in range(node_size):
        for j in range(node_size):
            d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j])
Q=int(input())
for _ in range(Q):
    s,t=map(int, input().split())
    s-=1
    t-=1
    c=d2[s][t]
    if c>=500:
        print(-1)
    else:
        print(max(0,c-1))
