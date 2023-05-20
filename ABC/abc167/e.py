from functools import reduce
MOD=998244353
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
N,M,K=map(int, input().split())
kaijou=[1]
for i in range(1,N):
    kaijou.append(kaijou[-1]*i%MOD)
ret=0
for i in range(K+1,N):
    r = kaijou[N-1] * ppow(kaijou[i], MOD-2)%MOD
    r = r * ppow(kaijou[N-i-1], MOD-2)%MOD
    r = r * M*ppow(M-1,N-1-i) %MOD
    ret+=r
    ret%=MOD
print((ppow(M,N)-ret+MOD)%MOD)
