MOD=998244353
N=int(input())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N*N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
ret=fn[N*N]
#print(ret)
for i in range(N*N-2*N+2):
    under=N-1+i
    upper=N*N-N-i
    #print((upper,under,under-N+1,upper-N+1))
    n0=fn[under]*fn_inv[under-N+1]%MOD
    n1=fn[upper]*fn_inv[upper-N+1]%MOD
    n2=fn[(N-1)*(N-1)]
    n=n0*n1%MOD*n2%MOD*N*N%MOD
    #print((n0,n1,n2))
    #print((i,n))
    ret-=n
    ret%=MOD
print(ret)
