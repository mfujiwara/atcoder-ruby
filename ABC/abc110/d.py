import collections
MOD=10**9+7
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
from functools import reduce
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
N,M=map(int, input().split())
if M==1:
    print(1)
    exit()
counts=collections.Counter(prime_factorize(M))
ret=1
for key in counts:
    n=counts[key]
    ret*=kaijou(n+N-1,n+1)
    ret%=MOD
    ret*=pow(kaijou(N-1,1),MOD-2,MOD)
    ret%=MOD
print(ret)
