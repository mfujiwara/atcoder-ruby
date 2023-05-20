import math
N,X=map(int, input().split())
array=list(map(int, input().split()))
ret=abs(array[0]-X)
for i in range(1,N):
    ret=math.gcd(ret,abs(array[i]-X))
print(ret)
