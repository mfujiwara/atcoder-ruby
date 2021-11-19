MOD=pow(10,9)+7
N,M,K=map(int, input().split())
ret1=N*(N*N-1)//6
ret1%=MOD
ret1*=M
ret1%=MOD
ret1*=M
ret1%=MOD
ret2=M*(M*M-1)//6
ret2%=MOD
ret2*=N
ret2%=MOD
ret2*=N
ret2%=MOD
ret=(ret1+ret2)%MOD
# (M*N-2)_C_(K-2)
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,M*N-1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
ret*=fn[M*N-2]
ret%=MOD
ret*=fn_inv[K-2]
ret%=MOD
ret*=fn_inv[M*N-K]
ret%=MOD
print(ret)
