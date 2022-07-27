import collections
N=int(input())
p_array=list(map(int, input().split()))
x_array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for i,p in enumerate(p_array):
    edges[p-1].append(i+1)
targets=[0]
nodes=[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        targets.append(u)
        nodes.append(u)
memo=[None]*N
while nodes:
    t=nodes.pop()
    sss=set([0])
    total=0
    for u in edges[t]:
        nexts=set()
        x=x_array[u]
        y=memo[u]
        total+=x+y
        for s in sss:
            if s+x<=x_array[t]:
                nexts.add(s+x)
            if s+y<=x_array[t]:
                nexts.add(s+y)
        sss=nexts
    if sss:
        memo[t]=total-max(sss)
    else:
        print("IMPOSSIBLE")
        exit()
print("POSSIBLE")
