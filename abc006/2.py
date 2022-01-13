MOD=10007
N=int(input())
dp=[0,0,0,1]
for i in range(4,N+1):
    dp.append((dp[-1]+dp[-2]+dp[-3])%MOD)
print(dp[N])
