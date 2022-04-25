MOD=998244353
N,M,K=map(int, input().split())
dp=[0]*(K+1)
for i in range(1,M+1):
    if i>=len(dp):
        break
    dp[i]+=1
# x=K-N+1
for i in range(N-1):
    nexts=[0]*(K+1)
    for d in range(1,M+1):
        if d>=len(dp):
            break
        for s in range(1,K+1):
            if d+s>=len(dp):
                break
            nexts[d+s]+=dp[s]
            nexts[d+s]%=MOD
    dp=nexts
ret=sum(dp)%MOD
print(ret)
