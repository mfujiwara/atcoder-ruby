import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
def distance(start):
    distances=[-1]*N
    distances[start]=0
    ret=start
    targets=[start]
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if distances[u]!=-1: continue
            distances[u]=distances[t]+1
            targets.append(u)
            if distances[u]>distances[ret]:
                ret=u
    return (ret,distances[ret])
t,_=distance(0)
_,d=distance(t)
if d%3==1:
    print("Second")
else:
    print("First")
