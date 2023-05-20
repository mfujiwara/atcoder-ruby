MOD=pow(10,9)+7
N,M=map(int, input().split())
dp=[0]*(N+1)
dp[0]=1
dp[1]=1
for _ in range(M):
    a=int(input())
    dp[a]=-1
if dp[1]==-1:
    dp[1]=0
for i in range(2,N+1):
    if dp[i]==-1:
        dp[i]=0
    else:
        dp[i]=dp[i-1]+dp[i-2]
        dp[i]%=MOD
print(dp[-1])
