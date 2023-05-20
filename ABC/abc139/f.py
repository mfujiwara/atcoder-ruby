import functools
import math
def quadrant(x,y):
    if y==0:
        if x>=0:
            return 1
        else:
            return 3
    if y>0:
        if x<=0:
            return 2
        else:
            return 1
    else:
        if x>=0:
            return 4
        else:
            return 3
def cmp(a,b):
    x0,y0,q0=a
    x1,y1,q1=b
    # (x0-y0)*(x1+y1)
    if q0!=q1:
        return q0-q1
    else:
        return -x0*y1+y0*x1
def degree(xy):
    x,y=xy
    if x==0:
        if y==0:
            return 0
        elif y>0:
            return 90
        else:
            return 270
    elif x>0:
        return (math.degrees(math.atan(y/x))+360)%360
    else:
        return (math.degrees(math.atan(y/x))+180)%360
N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y,quadrant(x,y)))
xy.sort(key=functools.cmp_to_key(cmp))
xy2=[(x,y,q+4) for x,y,q in xy]
xy=xy+xy2
ret=0
for start in range(N):
    sumX=0
    sumY=0
    for i in range(N):
        sumX+=xy[(start+i)%N][0]
        sumY+=xy[(start+i)%N][1]
        ret=max(ret,sumX*sumX+sumY*sumY)
print(pow(ret,0.5))
