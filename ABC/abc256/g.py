MOD=998244353
N,D=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,D):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]+=m1[i][k]*m2[k][j]%MOD
            ret[i][j]%=MOD
    return ret
def ppow(m,n):
    if n==0:
        mm=[[1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
ret=2
for d in range(1,D+1):
    # 1辺からd選ぶ
    # ox or xo
    X=fn[D-1]*fn_inv[d-1]%MOD*fn_inv[D-d]%MOD
    # oo
    if d==1:
        Y=0
    else:
        Y=fn[D-1]*fn_inv[d-2]%MOD*fn_inv[D-d+1]%MOD
    # xx
    if d==D:
        Z=0
    else:
        Z=fn[D-1]*fn_inv[d]%MOD*fn_inv[D-1-d]%MOD
    M=[[Y,X],[X,Z]]
    R=ppow(M,N)
    ret+=R[0][0]
    ret+=R[1][1]
    ret%=MOD
print(ret)
