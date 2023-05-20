import sys
import math
A,B,C=map(int, input().split())

l=0
r=200
while True:
    mid=(l+r)/2
    x=A*mid+B*math.sin(C*mid*math.pi)
    if abs(x-100)<=0.000001:
        print(mid)
        sys.exit()
    if x<100:
        l=mid
    else:
        r=mid
