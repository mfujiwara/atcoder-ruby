MOD=998244353
N,M=map(int, input().split())
binom=[[0]*2*N for _ in range(2*N)]
binom[0][0]=1
for i in range(1,2*N):
    binom[i][0]=1
    binom[i][i]=1
    for j in range(i-1):
        binom[i][j+1]=(binom[i-1][j]+binom[i-1][j+1])%MOD
pairs=[[0]*2*N for _ in range(2*N)]
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    pairs[a][b]=1
    pairs[b][a]=1
dp=[[1 if j==0 else 0 for j in range(N+1)] for _ in range(2*N+1)]
for j in range(1,N+1):
    for i in range(2*(N-j)+1):
        dp[i][j]=0
        for k in range(j):
            if pairs[i][i+(2*k)+1]:
                x=(dp[i+1][k] * dp[i+(2*k)+2][j-k-1])%MOD
                dp[i][j]=((x*binom[j][k+1])+dp[i][j])%MOD
print(dp[0][N])
