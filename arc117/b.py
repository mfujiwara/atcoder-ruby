MOD=10**9+7
N=int(input())
array=list(map(int, input().split()))
array=sorted(array)
array=[0]+array
ret=1
for i in range(N):
    ret*=(array[i+1]-array[i]+1)
    ret%=MOD
print(ret)
