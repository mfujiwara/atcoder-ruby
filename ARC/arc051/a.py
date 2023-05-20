import math
x1,y1,r=map(int, input().split())
x2,y2,x3,y3=map(int, input().split())
x2-=x1
x3-=x1
y2-=y1
y3-=y1

blue=False
for x in [x2,x3]:
    for y in [y2,y3]:
        if x*x+y*y>r*r:
            blue=True
if x2<=-r and r<=x3 and y2<=-r and r<=y3:
    red=False
else:
    red=True
print("YES" if red else "NO")
print("YES" if blue else "NO")
