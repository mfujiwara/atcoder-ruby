MOD=998244353
N=int(input())
dp=[1]*9
for i in range(N-1):
    nexts=[0]*9
    for i in range(9):
        if i>0:
            nexts[i-1]+=dp[i]
            nexts[i-1]%=MOD
        nexts[i]+=dp[i]
        nexts[i]%=MOD
        if i<8:
            nexts[i+1]+=dp[i]
            nexts[i+1]%=MOD
    dp=nexts
print(sum(dp)%MOD)
