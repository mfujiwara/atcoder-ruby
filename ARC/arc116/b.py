MOD=998244353
N=map(int, input().split())
array=list(map(int, input().split()))
base=0
array=sorted(array)
ret=0
for i,a in enumerate(array):
    ret+=base*a
    ret%=MOD
    ret+=a*a
    ret%=MOD
    base*=2
    base%=MOD
    base+=a
    base%=MOD
print(ret)
