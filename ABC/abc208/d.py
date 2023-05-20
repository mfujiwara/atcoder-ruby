INF=1<<60
N,M=map(int, input().split())
node_size=N
d = [[INF]*node_size for _ in range(node_size)]
base_cost=0
for _ in range(M):
    a,b,c=map(int, input().split())
    d[a-1][b-1]=c
    base_cost+=c
for i in range(N):
    d[i][i]=0
ret=0
for k in range(node_size):
    for i in range(node_size):
        for j in range(node_size):
            if i==j: continue
            old=d[i][j]
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if old!=d[i][j]:
                if old==INF:
                    base_cost+=d[i][j]
                else:
                    base_cost-=(old-d[i][j])
    ret+=base_cost
print(ret)
