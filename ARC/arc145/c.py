MOD=998244353
N=int(input())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,2*N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
ret=fn[2*N]
ret*=fn_inv[N]
ret%=MOD
ret*=inv[N+1]
ret%MOD
ret*=pow(2,N,MOD)
ret%=MOD
print(ret)
