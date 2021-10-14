import math
T=int(input())
L,X,Y=map(int, input().split())
Q=int(input())
for _ in range(Q):
    e=int(input())%T
    x=0
    y=-math.sin(e/T*2*math.pi)*L/2
    z=(1-math.cos(e/T*2*math.pi))*L/2
    xy=math.hypot(x-X,y-Y)
    if z==0:
        print(0)
    else:
        print(90-math.degrees(math.atan2(xy,z)))
