import bisect
import math
N=int(input())
rrr=[]
for i in range(N):
    x1,y1,x2,y2=map(int, input().split())
    r1=math.atan2(y1,x1)
    r2=math.atan2(y2,x2)
    if r1>r2:
        r1,r2=r2,r1
    if r2-r1>math.pi:
        r1,r2=r2,r1+math.pi*2
    rrr.append((r2,r1))
rrr.sort()
#print(rrr)
ret=N
for _ in range(N):
    c=0
    last_r2=-math.pi
    for r2,r1 in rrr:
        if r1>last_r2:
            last_r2=r2
            c+=1
    ret=min(ret,c)
    r2,r1=rrr.pop(0)
    rrr.append((r2+2*math.pi,r1+2*math.pi))
    rrr.sort()
print(ret)
