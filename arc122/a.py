MOD=10**9+7
N=int(input())
array=list(map(int, input().split()))
dp=[[(0,0)]*2 for _ in range(N)]
dp[0][0]=(array[0],1)
for i in range(1,N):
    c0=dp[i-1][0][1]+dp[i-1][1][1]
    c0%=MOD
    v0=dp[i-1][0][0]+dp[i-1][1][0]+c0*array[i]
    v0%=MOD
    dp[i][0]=(v0,c0)
    c1=dp[i-1][0][1]
    v1=dp[i-1][0][0]-c1*array[i]
    v1%=MOD
    dp[i][1]=(v1,c1)
ret=dp[-1][0][0]+dp[-1][1][0]
ret%=MOD
print(ret)
