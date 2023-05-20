import collections
from functools import reduce
MOD=998244353
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N,M=map(int, input().split())
memo={}
def h(k):
    if k in memo:
        return memo[k]
    # (n+k-1)C(k)
    v=kaijou(N+k-1,N)*ppow(kaijou(k,1),MOD-2)%MOD
    memo[k]=v
    return v
ret=1
for i in range(2,M+1):
    c = collections.Counter(prime_factorize(i))
    r=1
    for key in c:
        k=c[key]
        r*=h(k)
        r%=MOD
    ret+=r
    ret%=MOD
print(ret)
