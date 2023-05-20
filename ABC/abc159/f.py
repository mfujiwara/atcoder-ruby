MOD=998244353
N,S=map(int, input().split())
array=list(map(int, input().split()))
dp=[0]*S
ret=0
for i,a in enumerate(array):
    if a>S: continue
    if a==S:
        ret+=(i+1)*(N-i)%MOD
        ret%=MOD
        continue
    ret+=dp[S-a]*(N-i)%MOD
    ret%=MOD
    for b in range(S-a-1,0,-1):
        dp[b+a]+=dp[b]
    dp[a]+=i+1
print(ret)
