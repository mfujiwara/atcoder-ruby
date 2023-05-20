import collections
MOD=998244353
N=int(input())
array=list(map(int, input().split()))
last_index=collections.defaultdict(int)
dp=[0]*(N+1)
dp[1]=1
total=0
for i in range(1,N):
    total+=array[i-1]
    dp[i+1]=dp[i]*2%MOD
    index=last_index[total]
    dp[i+1]-=dp[index]
    dp[i+1]+=MOD
    dp[i+1]%=MOD
    last_index[total]=i
print(dp[-1])
