MOD=998244353
N,K=map(int, input().split())
dp=[[-1]*(n+1) for n in range(N+1)]
for n in range(1,N+1):
    for k in range(n,0,-1):
        if n==k:
            dp[n][k]=1
        else:
            v=0
            if n>=2*k:
                v+=dp[n][k*2]
            if k!=1:
                v+=dp[n-1][k-1]
            v%=MOD
            dp[n][k]=v
print(dp[N][K])
