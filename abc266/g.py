MOD=998244353
R,G,B,K=map(int, input().split())
RGB=R+G+B
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,RGB+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
r=R-K
g=G-K
# RG,G,Bの組み合わせ
ret=fn[K+g+B]*fn_inv[K]%MOD*fn_inv[g]%MOD*fn_inv[B]%MOD
# r個のRを入れる
ret1=fn[K+B+r]*fn_inv[K+B]%MOD*fn_inv[r]%MOD
ret=ret*ret1%MOD
print(ret)
