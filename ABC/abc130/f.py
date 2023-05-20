N=int(input())
fixed_maxX=None
fixed_minX=None
fixed_maxY=None
fixed_minY=None
down_maxX=None
down_minX=None
down_maxY=None
down_minY=None
up_maxX=None
up_minX=None
up_maxY=None
up_minY=None
for _ in range(N):
    x,y,d=input().split()
    x=int(x)
    y=int(y)
    if d=="R":
        if fixed_maxY==None:
            fixed_maxY=y
            fixed_minY=y
        else:
            fixed_maxY=max(fixed_maxY,y)
            fixed_minY=min(fixed_minY,y)
        if up_maxX==None:
            up_maxX=x
            up_minX=x
        else:
            up_maxX=max(up_maxX,x)
            up_minX=min(up_minX,x)
    elif d=="L":
        if fixed_maxY==None:
            fixed_maxY=y
            fixed_minY=y
        else:
            fixed_maxY=max(fixed_maxY,y)
            fixed_minY=min(fixed_minY,y)
        if down_maxX==None:
            down_maxX=x
            down_minX=x
        else:
            down_maxX=max(down_maxX,x)
            down_minX=min(down_minX,x)
    elif d=="U":
        if fixed_maxX==None:
            fixed_maxX=x
            fixed_minX=x
        else:
            fixed_maxX=max(fixed_maxX,x)
            fixed_minX=min(fixed_minX,x)
        if up_maxY==None:
            up_maxY=y
            up_minY=y
        else:
            up_maxY=max(up_maxY,y)
            up_minY=min(up_minY,y)
    else:
        if fixed_maxX==None:
            fixed_maxX=x
            fixed_minX=x
        else:
            fixed_maxX=max(fixed_maxX,x)
            fixed_minX=min(fixed_minX,x)
        if down_maxY==None:
            down_maxY=y
            down_minY=y
        else:
            down_maxY=max(down_maxY,y)
            down_minY=min(down_minY,y)
points=set([0])
# maxX
if fixed_maxX!=None and down_maxX!=None and fixed_maxX<down_maxX:
    points.add(down_maxX-fixed_maxX)
if fixed_maxX!=None and up_maxX!=None and fixed_maxX>up_maxX:
    points.add(fixed_maxX-up_maxX)
if down_maxX!=None and up_maxX!=None and down_maxX>up_maxX:
    points.add((down_maxX-up_maxX)/2)
# minX
if fixed_minX!=None and down_minX!=None and fixed_minX<down_minX:
    points.add(down_minX-fixed_minX)
if fixed_minX!=None and up_minX!=None and fixed_minX>up_minX:
    points.add(fixed_minX-up_minX)
if down_minX!=None and up_minX!=None and down_minX>up_minX:
    points.add((down_minX-up_minX)/2)
# maxY
if fixed_maxY!=None and down_maxY!=None and fixed_maxY<down_maxY:
    points.add(down_maxY-fixed_maxY)
if fixed_maxY!=None and up_maxY!=None and fixed_maxY>up_maxY:
    points.add(fixed_maxY-up_maxY)
if down_maxY!=None and up_maxY!=None and down_maxY>up_maxY:
    points.add((down_maxY-up_maxY)/2)
# minY
if fixed_minY!=None and down_minY!=None and fixed_minY<down_minY:
    points.add(down_minY-fixed_minY)
if fixed_minY!=None and up_minY!=None and fixed_minY>up_minY:
    points.add(fixed_minY-up_minY)
if down_minY!=None and up_minY!=None and down_minY>up_minY:
    points.add((down_minY-up_minY)/2)
ret=pow(10,17)
# print(sorted(points))
for p in points:
    maxXs=[]
    if fixed_maxX!=None:
        maxXs.append(fixed_maxX)
    if down_maxX!=None:
        maxXs.append(down_maxX-p)
    if up_maxX!=None:
        maxXs.append(up_maxX+p)
    minXs=[]
    if fixed_minX!=None:
        minXs.append(fixed_minX)
    if down_minX!=None:
        minXs.append(down_minX-p)
    if up_minX!=None:
        minXs.append(up_minX+p)
    maxYs=[]
    if fixed_maxY!=None:
        maxYs.append(fixed_maxY)
    if down_maxY!=None:
        maxYs.append(down_maxY-p)
    if up_maxY!=None:
        maxYs.append(up_maxY+p)
    minYs=[]
    if fixed_minY!=None:
        minYs.append(fixed_minY)
    if down_minY!=None:
        minYs.append(down_minY-p)
    if up_minY!=None:
        minYs.append(up_minY+p)
    r=(max(maxXs)-min(minXs))*(max(maxYs)-min(minYs))
    # print(p,r)
    # print(max(maxXs),min(minXs),max(maxYs),min(minYs))
    ret=min(ret,r)
print(ret)
