import math
import sys
N,M=map(int, input().split())
array=list(map(int, input().split()))
k=2
a=array[0]//2
while a%2==0:
    a//=2
    k*=2
# X= a * (p + 0.5)
lcm=1
for a in array:
    q,r=divmod(a,k)
    if q%2==0 or r!=0:
        print(0)
        sys.exit()
    lcm=lcm*a//math.gcd(lcm,a)
print(M//(lcm//2)-M//lcm)
