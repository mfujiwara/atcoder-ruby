import collections
N,X=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(N-1):
    x,y,c=map(int, input().split())
    x-=1
    y-=1
    edges[x].append((y,c))
    edges[y].append((x,c))
counts=collections.defaultdict(int)
counts[0]+=1
targets=[(0,0)]
done=[False]*N
done[0]=True
while targets:
    t,v=targets.pop()
    for u,c in edges[t]:
        if done[u]: continue
        done[u]=True
        w=v^c
        counts[w]+=1
        targets.append((u,w))
ret=0
if X==0:
    for key in counts:
        c=counts[key]
        ret+=c*(c-1)//2
else:
    for key in list(counts.keys()):
        c=counts[key]
        d=counts[key^X]
        ret+=c*d
    ret//=2
print(ret)
