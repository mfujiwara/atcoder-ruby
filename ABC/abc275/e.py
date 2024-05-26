N,M,K=map(int, input().split())
MOD=998244353
invM=pow(M,MOD-2,MOD)
dp=[0]*(N+1)
dp[0]=1
for _ in range(K):
    nexts=[0]*(N+M)
    nexts[N]=dp[N]
    for i in range(N):
        for j in range(1,M+1):
            nexts[i+j]+=dp[i]*invM%MOD
            nexts[i+j]%=MOD
    for i in range(M-1):
        nexts[N-1-i]+=nexts[N+1+i]
        nexts[N-1-i]%=MOD
    dp=nexts
print(dp[N])
