import math
N,K=map(int, input().split())
array=list(map(int, input().split()))
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
mins=[pow(10,10)]*N
for i,xxyy in enumerate(xy):
    x0,y0=xxyy
    for a in array:
        x,y=xy[a-1]
        mins[i]=min(mins[i],math.hypot(x0-x,y0-y))
print(max(mins))
