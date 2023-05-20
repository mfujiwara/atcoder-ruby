MOD=998244353
N,M=map(int, input().split())
ret=pow(N,M,MOD)*pow(M,N-1,MOD)%MOD
print(ret)
