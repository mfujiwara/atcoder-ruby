import sys
MOD=998244353
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x

N,M,K=map(int, input().split())
if N==1:
    ret=ppow(K,M)%MOD
    print(ret)
    sys.exit()
if M==1:
    ret=ppow(K,N)%MOD
    print(ret)
    sys.exit()
ret=0
for k in range(1,K+1):
    ret+=(ppow(k,N)-ppow(k-1,N)) * ppow(K-k+1,M)
    ret%=MOD
print(ret)
