MOD=pow(10,9)+7
N,M,K=map(int, input().split())
if N>M+K:
    print(0)
    exit()
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for i in range(2,max(N+M,N+K+1)+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    fn_inv.append(fn_inv[-1]*inv[i]%MOD)
total=fn[N+M]*pow(fn[M]*fn[N],MOD-2,MOD)%MOD
minus=0
if N-K>=1:
    minus=fn[N+M]*pow(fn[M+K+1]*fn[N-K-1],MOD-2,MOD)%MOD
ret=(total-minus+MOD)%MOD
print(ret)
