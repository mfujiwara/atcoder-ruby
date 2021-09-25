import math
N=int(input())
gx1=gy1=0
xy1=[]
for _ in range(N):
    x,y=map(int, input().split())
    gx1+=x
    gy1+=y
    xy1.append((x,y))
gx1/=N
gy1/=N
d1=0
for x,y in xy1:
    d1=max(d1,math.hypot(x-gx1,y-gy1))
gx2=gy2=0
xy2=[]
for _ in range(N):
    x,y=map(int, input().split())
    gx2+=x
    gy2+=y
    xy2.append((x,y))
gx2/=N
gy2/=N
d2=0
for x,y in xy2:
    d2=max(d2,math.hypot(x-gx2,y-gy2))
print(d2/d1)
