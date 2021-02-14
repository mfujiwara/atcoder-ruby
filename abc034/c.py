from functools import reduce
MOD=10**9+7
W,H=map(int, input().split())
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
print((kaijou(W+H-2,W) * ppow(kaijou(H-1,1), MOD-2))%MOD)
