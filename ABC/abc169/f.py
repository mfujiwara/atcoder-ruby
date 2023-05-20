MOD=998244353
N,S=map(int, input().split())
array=list(map(int, input().split()))
dp=[[0]*(S+1) for _ in range(N+1)]
dp[0][0]=1
for i,a in enumerate(array):
    for s in range(S+1):
        dp[i+1][s]=dp[i][s]*2
        dp[i+1][s]%=MOD
        if s>=a:
            dp[i+1][s]+=dp[i][s-a]
            dp[i+1][s]%=MOD
print(dp[-1][-1])
