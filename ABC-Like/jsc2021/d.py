MOD=10**9+7
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
N,P=map(int, input().split())
ret=(P-1)*ppow(P-2, N-1)%MOD
print(ret)
