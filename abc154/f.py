MOD=10**9+7
r1,c1,r2,c2=list(map(int, input().split()))
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for i in range(2,r2+c2+3):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
def gn(r,c):
    v=fn[r+c+2]*fn_inv[r+1]%MOD
    v=v*fn_inv[c+1]%MOD
    v%=MOD
    return v
c22=gn(r2,c2)
c21=gn(r2,c1-1)
c12=gn(r1-1,c2)
c11=gn(r1-1,c1-1)
print((c22-c21-c12+c11+MOD)%MOD)
