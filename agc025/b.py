MOD=998244353
N,A,B,K=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for i in range(2,N+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
ret=0
for a in range(K//A+1):
    b,r=divmod(K-A*a,B)
    if r!=0 or a>N or b>N: continue
    r1=fn[N]*fn_inv[a]*fn_inv[N-a]%MOD
    r2=fn[N]*fn_inv[b]*fn_inv[N-b]%MOD
    ret+=r1*r2%MOD
    ret%=MOD
print(ret)
