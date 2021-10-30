MOD=998244353
S=input()
N=len(S)
dp=[1,11]
for i in range(2,N):
    dp.append(dp[-1]*10%MOD+pow(2,i-1,MOD))
ret=0
for i,ch in enumerate(S):
    s=int(ch)
    r=s*dp[N-1-i]%MOD
    r*=pow(2,i,MOD)
    r%=MOD
    ret+=r
    ret%=MOD
print(ret)
