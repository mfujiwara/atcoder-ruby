MOD=998244353
N,M,K=map(int, input().split())
invalids=set()
for _ in range(M):
    u,v=map(int, input().split())
    invalids.add((u-1,v-1))
    #invalids.add((v-1,u-1))
dp=[[0]*N for _ in range(K+1)] # dp[i][j]:=i日目に都市jにいる場合の数
dp[0][0]=1
pre_sum=1
for i in range(1,K+1):
    for j in range(N):
        dp[i][j]=pre_sum-dp[i-1][j]
        dp[i][j]%=MOD
    for u,v in invalids:
        dp[i][u]-=dp[i-1][v]
        dp[i][u]%=MOD
        dp[i][v]-=dp[i-1][u]
        dp[i][v]%=MOD
    pre_sum=sum(dp[i])
    pre_sum%=MOD
print((dp[K][0]+MOD)%MOD)
