MOD=pow(10,9)+7
N,M=map(int, input().split())
fn=[1,1]
inv=[1,1]
inv_fn=[1,1]
for i in range(2,M+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    inv_fn.append(inv_fn[-1]*inv[-1]%MOD)
ret=0
for i in range(N+1):
    v=fn[N]*inv_fn[i]%MOD
    v=v*inv_fn[N-i]%MOD
    v=v*pow(-1,i)
    v=v*fn[M]%MOD
    v=v*inv_fn[M-i]%MOD
    v=v*fn[M-i]%MOD
    v=v*inv_fn[M-N]%MOD
    v=v*fn[M-i]%MOD
    v=v*inv_fn[M-N]%MOD
    ret+=v
    ret+=MOD
    ret%=MOD
print(ret)
