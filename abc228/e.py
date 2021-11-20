MOD=998244353
N,K,M=map(int, input().split())
num=pow(K,N,MOD-1)
if num==0:
    num=MOD-1
ret=pow(M,num,MOD)
print(ret)
