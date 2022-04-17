import collections
N=int(input())
edges=collections.defaultdict(list)
children=collections.defaultdict(list)
for _ in range(N-1):
    x,y=map(int, input().split())
    x-=1
    y-=1
    edges[x].append(y)
    edges[y].append(x)
nims=[0]*N
status=[0]*N
targets=[0]
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
                children[t].append(u)
    else:
        v=0
        for u in children[t]:
            v^=nims[u]
        nims[t]=v+1
if nims[0]==1:
    print("Bob")
else:
    print("Alice")
