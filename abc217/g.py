MOD=998244353
N,M=map(int, input().split())
dp=[[0]*N for _ in range(N)]
dp[0][0]=1
for i in range(1,N):
    for j in range(N):
        if j==0:
            if i<M:
                dp[i][j]=1
        else:
            dp[i][j]=(dp[i-1][j-1]+(j+1-i//M)*dp[i-1][j]%MOD)%MOD
for i in range(N):
    print(dp[-1][i])
