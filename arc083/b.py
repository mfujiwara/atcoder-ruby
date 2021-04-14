import sys
INF=10**9
N=int(input())
d=[list(map(int, input().split())) for _ in range(N)]
done=[[False]*N for _ in range(N)]
ret=sum(sum(d,[]))//2
for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k] + d[k][j]:
                print(-1)
                sys.exit()
            if i!=j and j!=k and k!=i and i>j and not done[i][j] and d[i][j]==d[i][k]+d[k][j]:
                ret-=d[i][j]
                done[i][j]=True
print(ret)
