import functools
MOD=10**9+7
N=int(input())
array=list(map(int, input().split()))
base=1
inv=[1,1]
for i in range(2,N):
    base*=i
    base%=MOD
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
fn=[1]
ret=0
k=0
for i in range(N-1):
    d=array[i+1]-array[i]
    k+=base*inv[i+1]
    k%=MOD
    ret+=d*k
    ret%=MOD
print(ret)
