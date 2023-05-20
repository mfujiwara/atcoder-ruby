import collections
import itertools
H,W,N=map(int, input().split())
rc=[]
arc=[]
rets={}
r_max=collections.defaultdict(lambda: -1)
c_max=collections.defaultdict(lambda: -1)
for _ in range(N):
    r,c,a=map(int, input().split())
    rc.append((r,c))
    arc.append((a,r,c))
grouped=collections.defaultdict(list)
for a,r,c in arc:
    grouped[a].append((a,r,c))

for key in sorted(list(grouped.keys()), reverse=True):
    r_stack=[]
    c_stack=[]
    for a,r,c in grouped[key]:
        ret=max(r_max[r],c_max[c])+1
        rets[(r,c)]=ret
        r_stack.append((r,ret))
        c_stack.append((c,ret))
    for r,v in r_stack:
        r_max[r]=max(r_max[r],v)
    for c,v in c_stack:
        c_max[c]=max(c_max[c],v)
for e in rc:
    print(rets[e])
