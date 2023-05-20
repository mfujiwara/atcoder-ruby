MOD=998244353
# 1,3,10,35
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
from functools import reduce
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
d=int(input())
inv2=MOD - 1 * (MOD // 2) % MOD
v=kaijou(2*d,d+1)*ppow(kaijou(d,1),MOD-2)%MOD
v=v*inv2%MOD
print(v)
