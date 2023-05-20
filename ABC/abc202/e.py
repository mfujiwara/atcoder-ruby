from collections import defaultdict, deque
import bisect
import sys
sys.setrecursionlimit(500000)
N=int(input())
array=list(map(int, input().split()))
edges=defaultdict(list)
for i in range(N-1):
    array[i]-=1
    edges[array[i]].append(i+1)
nodes=[[-1,-1] for _ in range(N)]
depths=[[] for _ in range(N)]
targets=[(0,True,0)]
c=0
while targets:
    t,tb,td=targets.pop()
    if tb:
        nodes[t][0]=c
        c+=1
        targets.append((t,False,td))
        for child in edges[t]:
            targets.append((child,True,td+1))
    else:
        nodes[t][1]=c
        c+=1
        depths[td].append(nodes[t][0])
        depths[td].append(nodes[t][1])
Q=int(input())
for _ in range(Q):
    u,d=map(int, input().split())
    border=nodes[u-1]
    depth=depths[d]
    left=bisect.bisect_left(depth,border[0])
    right=bisect.bisect_right(depth,border[1])
    print((right-left)//2)
