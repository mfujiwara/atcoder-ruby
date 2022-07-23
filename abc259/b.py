import math
a,b,d=map(int, input().split())
x=math.cos(math.radians(d))
y=math.sin(math.radians(d))
print(a*x-b*y,a*y+b*x)
