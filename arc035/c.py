INF=1<<60
N,M=map(int, input().split())
node_size=N
d = [[INF]*node_size for _ in range(node_size)]
for _ in range(M):
    a,b,c=map(int, input().split())
    d[a-1][b-1]=c
    d[b-1][a-1]=c
for i in range(N):
    d[i][i]=0
for k in range(node_size):
    for i in range(node_size):
        for j in range(node_size):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
S=sum(map(sum, d))
K=int(input())
for _ in range(K):
    x,y,z=map(int, input().split())
    if d[x-1][y-1]>z:
        S-=(d[x-1][y-1]-z)*2
        d[x-1][y-1]=z
        d[y-1][x-1]=z
        for k in [x-1,y-1]:
            for i in range(node_size-1):
                for j in range(i+1,node_size):
                    if d[i][j] > d[i][k] + d[k][j]:
                        S-=(d[i][j] - d[i][k] - d[k][j])*2
                        d[i][j] = d[i][k] + d[k][j]
                        d[j][i] = d[i][j]
                        
    print(S//2)
