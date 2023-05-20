import math
A,B=map(int, input().split())
g=math.gcd(A,B)
ret=A//g*B
if ret>pow(10,18):
    print("Large")
else:
    print(ret)
