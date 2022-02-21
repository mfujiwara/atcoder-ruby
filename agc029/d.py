import bisect
import collections
H,W,N=map(int, input().split())
xy=[]
xy_set=set()
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
    xy_set.add((x,y))
xy.sort(key=lambda e: e[0])
dots=collections.defaultdict(list)
for x,y in xy:
    dots[y].append(x)
for w in range(1,W+1):
    dots[w].append(H+1)
cur_x=1
cur_y=1
ret=H
while cur_x<H+1 and cur_y<W+1:
    xx=bisect.bisect(dots[cur_y],cur_x)
    ret=min(ret,dots[cur_y][xx]-1)
    cur_x+=1
    while (cur_x,cur_y+1) in xy_set:
        cur_x+=1
    cur_y+=1
print(ret)
