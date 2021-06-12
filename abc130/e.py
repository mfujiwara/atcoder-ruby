MOD=10**9+7
N,M=map(int, input().split())
s_array=list(map(int, input().split()))
t_array=list(map(int, input().split()))
dp=[[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0]=1
for i in range(M+1):
    dp[0][i]=1
for i in range(1,N+1):
    for j in range(1,M+1):
        if s_array[i-1]==t_array[j-1]:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
        dp[i][j]%=MOD
print(dp[-1][-1])
