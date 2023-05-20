import itertools
MOD=998244353
N,M,K=map(int, input().split())
dp=[1]*(M+1)
dp[0]=0
for _ in range(N-1):
    nexts=[0]*(M+1)
    sums=[0]*(M+1)
    for i in range(1,M+1):
        sums[i]=(sums[i-1]+dp[i])%MOD
    for i in range(1,M+1):
        if K==0:
            nexts[i]+=sums[M]
        else:
            if i>K:
                nexts[i]+=sums[i-K]
                nexts[i]%=MOD
            if i<=M-K:
                nexts[i]+=sums[M]
                nexts[i]%=MOD
                nexts[i]-=sums[i+K-1]
                nexts[i]%=MOD
    dp=nexts
    #print(dp)
sums=[0]*(M+1)
for i in range(1,M+1):
    sums[i]=(sums[i-1]+dp[i])%MOD
ret=sums[-1]
print(ret)
