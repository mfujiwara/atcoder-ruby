from functools import reduce
MOD=10**9+7
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
n=int(input())
k=int(input())
fn=[1,1]
inv=[1,1]
inv_fn=[1,1]
for i in range(2,max(k,n+1)):
    fn.append(fn[-1]*i%MOD)
    r=MOD - inv[MOD % i] * (MOD // i) % MOD
    inv.append(r)
    inv_fn.append(inv_fn[-1]*r%MOD)

ret=0
for i in range(min(n,k)):
    r=fn[n]
    r=r*inv_fn[i+1]%MOD
    r=r*inv_fn[n-i-1]%MOD
    #kをi+1個に分ける (k-1)_C_i
    r=r*fn[k-1]%MOD
    r=r*inv_fn[i]%MOD
    r=r*inv_fn[k-1-i]%MOD
    ret+=r
    ret%=MOD
print(ret)
