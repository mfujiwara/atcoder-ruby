import math
N=int(input())
ret=1
for _ in range(N):
    t=int(input())
    ret=ret*t//math.gcd(ret,t)
print(ret)
