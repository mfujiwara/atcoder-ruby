import math
a,b,c=map(int, input().split())
r1=a+b+c
if a+b<c or b+c<a or c+a<b:
    abc=sorted([a,b,c])
    r2=abc[2]-abc[0]-abc[1]
else:
    r2=0
print(math.pi*r1*r1-math.pi*r2*r2)
