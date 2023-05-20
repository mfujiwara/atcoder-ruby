MOD=998244353
N,K=map(int, input().split())
array=list(map(int, input().split()))
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,max(N+1,K+1)):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
memo=[0]*(K+1)
for i in range(N):
    v=1
    for k in range(K+1):
        memo[k]+=v*fn_inv[k]%MOD
        memo[k]%=MOD
        v*=array[i]
        v%=MOD
memo2=[0]*(K+1)
for i in range(N):
    v=1
    for k in range(K+1):
        memo2[k]+=v
        memo2[k]%=MOD
        v*=2*array[i]
        v%=MOD
for x in range(1,K+1):
    ret=0
    for k in range(x+1):
        ret+=memo[k]*memo[x-k]%MOD
        ret%=MOD
    ret*=fn[x]
    ret%=MOD
    ret+=MOD-memo2[x]
    ret%=MOD
    ret*=inv[2]
    ret%=MOD
    print(ret)
