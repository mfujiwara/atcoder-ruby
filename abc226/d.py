import math
N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
rets=set()
for i in range(N-1):
    for j in range(i+1,N):
        x1,y1=xy[i]
        x2,y2=xy[j]
        dx=x1-x2
        dy=y1-y2
        if dx==0:
            rets.add((0,1))
            rets.add((0,-1))
        elif dy==0:
            rets.add((1,0))
            rets.add((-1,0))
        else:
            g=math.gcd(dx,dy)
            dx//=g
            dy//=g
            rets.add((dx,dy))
            rets.add((-dx,-dy))
print(len(rets))
