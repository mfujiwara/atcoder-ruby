MOD=998244353
import functools
def kaijou(a, b):
    return functools.reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
N,K=map(int, input().split())
array=list(map(int, input().split()))
if array[0]<sum(array[1:])+K:
    print(0)
    exit()
kkk=pow(kaijou(K-1,1),MOD-2,MOD)
ret=pow(kkk,N,MOD)
array[0]=array[0]-sum(array[1:])-K
for a in array:
    ret*=kaijou(a+K-1,a+1)
    ret%=MOD
print(ret)
