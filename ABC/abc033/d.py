import bisect
import math
EPS=pow(0.1,10)
N=int(input())
xy=[]
for _ in range(N):
    xy.append(tuple(map(int,input().split())))
choku=0
don=0
for i in range(N):
    l1,l2 = [],[]
    xi,yi = xy[i]
    for j in range(N):
        if i!= j:
            x,y = xy[j]
            rad = math.atan2(y-yi,x-xi)
            l1.append(rad)
            l2.append(rad)
            l2.append(rad + 2*math.pi)
    l2.sort()
    for rad in l1:
        choku += bisect.bisect_left(l2,rad+math.pi/2+EPS) - bisect.bisect_left(l2,rad+math.pi/2-EPS)
        don += bisect.bisect_left(l2,rad+math.pi-EPS) - bisect.bisect_left(l2,rad+math.pi/2+EPS)
print(N*(N-1)*(N-2)//6 - choku - don,choku,don)
