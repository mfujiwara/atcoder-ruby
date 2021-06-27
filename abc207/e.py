import itertools
MOD=10**9+7
N=int(input())
array=list(map(int, input().split()))
sums=[0]+list(itertools.accumulate(array))
dp=[[0]*(N+1) for i in range(N+1)]
dp[0][0]=1
for i in range(1,N+1):
    mods=[0]*i
    for j in range(0,N+1):
        dp[i][j]=mods[sums[j]%i]
        dp[i][j]%=MOD
        mods[sums[j]%i]+=dp[i-1][j]
ret=0
for d in dp:
    ret+=d[-1]
print(ret%MOD)
