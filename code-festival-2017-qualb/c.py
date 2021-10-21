import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
group=[0]*N
group[0]=1
targets=[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        if group[u]==0:
            group[u]=group[t]*(-1)
            targets.append(u)
        else:
            if group[u]==group[t]:
                print(N*(N-1)//2-M)
                exit()
gc=0
for g in group:
    if g==1:
        gc+=1
print(gc*(N-gc)-M)
