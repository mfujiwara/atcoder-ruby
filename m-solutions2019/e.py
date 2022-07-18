MOD=1000003
Q=int(input())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,MOD):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
for _ in range(Q):
    X,D,N=map(int, input().split())
    if D==0:
        print(pow(X,N,MOD))
    else:
        base=X*inv[D]%MOD
        if base+N-1>=MOD:
            print(0)
        else:
            ret=fn[base+N-1]*fn_inv[base-1]%MOD*pow(D,N,MOD)%MOD
            print(ret)
