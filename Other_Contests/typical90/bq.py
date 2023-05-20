MOD=pow(10,9)+7
N,K=map(int, input().split())
if N==1:
    print(K)
else:
    base=K*(K-1)%MOD
    print(base*pow(K-2,N-2,MOD)%MOD)
