import collections
import bisect
H,W,rs,cs=map(int, input().split())
N=int(input())
wall_r=collections.defaultdict(lambda: [0,W+1])
wall_c=collections.defaultdict(lambda: [0,H+1])
for _ in range(N):
    r,c=map(int, input().split())
    wall_r[r].append(c)
    wall_c[c].append(r)
for key in list(wall_r.keys()):
    wall_r[key]=sorted(wall_r[key])
for key in list(wall_c.keys()):
    wall_c[key]=sorted(wall_c[key])
Q=int(input())
for _ in range(Q):
    d,l=input().split()
    l=int(l)
    if d=="L":
        i=bisect.bisect(wall_r[rs],cs)
        t=wall_r[rs][i-1]
        cs=max(cs-l,t+1)
    elif d=="R":
        i=bisect.bisect(wall_r[rs],cs)
        t=wall_r[rs][i]
        cs=min(cs+l,t-1)
    elif d=="U":
        i=bisect.bisect(wall_c[cs],rs)
        t=wall_c[cs][i-1]
        rs=max(rs-l,t+1)
    else:
        i=bisect.bisect(wall_c[cs],rs)
        t=wall_c[cs][i]
        rs=min(rs+l,t-1)
    print(rs,cs)


