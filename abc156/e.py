from functools import reduce
MOD=10**9+7
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x

# 階乗(a > b)
def kaijou(a, b):
    return reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)

N,K=map(int, input().split())
f=[1,1]
inv=[0,1]
f_inv=[1,1]
for i in range(2,N+2):
    f.append(f[-1]*i%MOD)
    inv.append(MOD-inv[MOD%i]*(MOD//i)%MOD)
    f_inv.append(f_inv[-1]*inv[-1]%MOD)
ret=0
for i in range(min(K+1,N)):
    #n_C_i * n+1_C_i
    r=f[N]*f_inv[i]%MOD
    r=r*f_inv[N-i]%MOD
    r=r*f[N-1]%MOD
    r=r*f_inv[i]%MOD
    r=r*f_inv[N-i-1]%MOD
    ret+=r
    ret%=MOD
print(ret)
