import math
N=int(input())
array=list(map(int, input().split()))
ret=array[0]
for i in range(1,N):
    ret=math.gcd(ret,array[i])
print(ret)
