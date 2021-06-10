import math
DELTA=pow(10,-7)
def judge(xy, R):
    crosses=[]
    for i in range(N-1):
        x1,y1=xy[i]
        for j in range(i+1,N):
            x2,y2=xy[j]
            l=math.hypot(x1-x2,y1-y2)
            h=l/2
            if h>R:
                return False
            xc,yc=(x1+x2)/2,(y1+y2)/2
            r=math.sqrt(R*R-h*h)
            x3=xc+(y1-y2)*r/l
            y3=yc+(x2-x1)*r/l
            x4=xc+(y2-y1)*r/l
            y4=yc+(x1-x2)*r/l
            crosses.append((x3,y3))
            crosses.append((x4,y4))
    for xx,yy in crosses:
        if all([math.hypot(x-xx,y-yy)<R+DELTA for x,y in xy]):
            return True
    return False
N=int(input())
xy=[list(map(int, input().split())) for _ in range(N)]
if N==2:
    print(math.hypot(xy[0][0]-xy[1][0],xy[0][1]-xy[1][1])/2)
    exit()
left=0
right=1000
while True:
    if right-left<DELTA:
        print(left)
        exit()
    mid=(left+right)/2
    if judge(xy, mid):
        right=mid
    else:
        left=mid
