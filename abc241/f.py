import bisect


import bisect
import collections
H,W,N=map(int, input().split())
sx,sy=map(int, input().split())
gx,gy=map(int, input().split())
x_walls=collections.defaultdict(list)
y_walls=collections.defaultdict(list)
done=collections.defaultdict(set)
for _ in range(N):
    x,y=map(int, input().split())
    x_walls[x].append(y)
    y_walls[y].append(x)
for key in list(x_walls.keys()):
    x_walls[key].sort()
for key in list(y_walls.keys()):
    y_walls[key].sort()
targets=set([(sx,sy)])
done[sx].add(sy)
ret=0
while targets:
    nexts=set()
    for tx,ty in targets:
        if tx==gx and ty==gy:
            print(ret)
            exit()
        if len(y_walls[ty])>0:
            index=bisect.bisect(y_walls[ty],tx)
            if index!=0:
                ux=y_walls[ty][index-1]+1
                uy=ty
                if uy not in done[ux]:
                    nexts.add((ux,uy))
                    done[ux].add(uy)
            if index!=len(y_walls[ty]):
                ux=y_walls[ty][index]-1
                uy=ty
                if uy not in done[ux]:
                    nexts.add((ux,uy))
                    done[ux].add(uy)
        if len(x_walls[tx])>0:
            index=bisect.bisect(x_walls[tx],ty)
            if index!=0:
                ux=tx
                uy=x_walls[tx][index-1]+1
                if uy not in done[ux]:
                    nexts.add((ux,uy))
                    done[ux].add(uy)
            if index!=len(x_walls[tx]):
                ux=tx
                uy=x_walls[tx][index]-1
                if uy not in done[ux]:
                    nexts.add((ux,uy))
                    done[ux].add(uy)
    targets=nexts
    ret+=1
print(-1)
