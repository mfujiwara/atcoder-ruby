MOD=998244353
N,M=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,3*M+N):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD) 
if N==2:
    print(M+1)
    exit()
# 全部足したら 3M な配列の場合の数
ret=fn[3*M+N-1]*fn_inv[N-1]%MOD*fn_inv[3*M]
# ある数が 2M+1 以上になる場合の数を引く
for i in range(2*M+1,3*M+1):
    ret-=N*fn[3*M-i+N-2]%MOD*fn_inv[N-2]%MOD*fn_inv[3*M-i]
    ret%=MOD
# 奇数が M 個より多い場合の数を引く
for i in range(M):
    # 偶数に使う合計が i*2
    # 奇数の項が 3*M-i*2 個
    if 3*M-i*2<=N:
        v=fn[i+N-1]*fn_inv[N-1]%MOD*fn_inv[i]
        v*=fn[N]*fn_inv[3*M-i*2]%MOD*fn_inv[N-3*M+i*2]
        ret-=v
        ret%=MOD
print(ret)
