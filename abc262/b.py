N,M=map(int, input().split())
edges=[[False]*N for _ in range(N)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u][v]=True
    edges[v][u]=True
ret=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if edges[i][j] and edges[j][k] and edges[k][i]:
                ret+=1
print(ret)
