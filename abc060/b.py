import math
A,B,C=map(int, input().split())
# x*B+C=A*y
if C%math.gcd(A,B)==0:
    print("YES")
else:
    print("NO")
