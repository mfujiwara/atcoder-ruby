MOD=10**9+7
N=int(input())
array=list(map(int, input().split()))
array.sort()
ret=1
for i,a in enumerate(array):
    ret*=a-i
    ret%=MOD
print(ret)
