import math
N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
for i in range(N):
    x0,y0=xy[i]
    xxyy=set()
    for j in range(N):
        if i==j: continue
        xx,yy=xy[j]
        xx-=x0
        yy-=y0
        g=math.gcd(xx,yy)
        x1=xx//g
        y1=yy//g
        if x1*xx<0 or y1*yy<0:
            x1*=-1
            y1*=-1
        xxyy.add((x1,y1))
    if len(xxyy)==1:
        print(0.5)
    else:
        def calc():
            x1,y1=xxyy.pop()
            x2,y2=xxyy.pop()
            # (x1+y1)*(x2-y2)            
            while xxyy:
                x3,y3=xxyy.pop()
                
                x12=x1*x2+y1*y2
                y12=x2*y1-x1*y2
                x23=x2*x3+y2*y3
                y23=x3*y2-x2*y3
                x31=x3*x1+y3*y1
                y31=x1*y3-x3*y1
                if y12>=0 and y23>=0 and y31>=0:
                    #print((x1,y1),(x2,y2),(x3,y3))
                    #print((x12,y12),(x23,y23),(x31,y31))
                    return "0.0"
                if y12<=0 and y23<=0 and y31<=0:
                    #print((x1,y1),(x2,y2),(x3,y3))
                    #print((x12,y12),(x23,y23),(x31,y31))
                    return "0.0"
                d12=x12**2+y12**2
                d23=x23**2+y23**2
                d31=x31**2+y31**2

                xx12=x12*abs(x12)
                xx23=x23*abs(x23)
                xx31=x31*abs(x31)
                if xx23*d31<=xx31*d23 and xx23*d12<=xx12*d23:
                    x1=x3
                    y1=y3
                elif xx31*d12<=xx12*d31 and xx31*d23<=xx23*d31:
                    x2=x3
                    y2=y3
            x12=x1*x2+y1*y2
            y12=x2*y1-x1*y2
            return (math.pi-math.acos(x12/math.hypot(x12,y12)))/math.pi*0.5
        print(calc())
