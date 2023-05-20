import math
a,b,x=map(int, input().split())
if a*a*b<=x*2:
    y=a*a*b-x
    h=y/a/a*2
    left=0
    right=90
    for _ in range(100):
        if abs(y*2*math.cos(left/180*math.pi)-a*a*a*math.sin(left/180*math.pi))<10**(-6):
            print(left)
            exit()
        mid=(left+right)/2
        if y*2*math.cos(mid/180*math.pi)-a*a*a*math.sin(mid/180*math.pi)>0:
            left=mid
        else:
            right=mid
else:
    y=x/a/b*2
    left=0
    right=90
    while True:
        if abs(b*math.cos(left/180*math.pi)-y*math.sin(left/180*math.pi))<10**(-6):
            print(left)
            exit()
        mid=(left+right)/2
        if b*math.cos(mid/180*math.pi)-y*math.sin(mid/180*math.pi)>0:
            left=mid
        else:
            right=mid
