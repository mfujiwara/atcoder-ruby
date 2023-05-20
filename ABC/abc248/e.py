import collections
import math
N,K=map(int, input().split())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
if K==1:
    print("Infinity")
    exit()
rets=collections.defaultdict(int)
for i in range(N):
    x0,y0=xy[i]
    counts=collections.defaultdict(int)
    for j in range(N):
        if i==j: continue
        x,y=xy[j]
        x-=x0
        y-=y0
        g=math.gcd(x,y)
        x//=g
        y//=g
        if y<0 or y==0 and x<0:
            x=-x
            y=-y
        counts[(x,y)]+=1
    for key in counts:
        if counts[key]>=K-1:
            rets[counts[key]+1]+=1
ret=0
for key in rets:
    ret+=rets[key]//key
print(ret)
