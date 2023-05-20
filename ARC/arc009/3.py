MOD=1777777777
import functools
def kaijou(a, b):
    return functools.reduce(lambda i, j: (i%MOD)*(j%MOD)%MOD, range(b,a+1), 1)
N,K=map(int, input().split())
montmort=[0,1]
for i in range(3,K+1):
    montmort=[montmort[-1],(i-1)*(sum(montmort)%MOD)%MOD]
ret=kaijou(N,N-K+1)*pow(kaijou(K,1),MOD-2,MOD)%MOD
ret*=montmort[-1]
ret%=MOD
print(ret)
