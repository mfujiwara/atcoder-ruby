import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
def calc(start):
    distances=[-1]*N
    distances[start]=0
    ret=start
    targets=[start]
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if distances[u]!=-1: continue
            distances[u]=distances[t]+1
            if distances[u]>distances[ret]:
                ret=u
            targets.append(u)
    return (ret,distances)
tt,_=calc(0)
uu,distances=calc(tt)
shortest=[uu]
done=[False]*N
done[uu]=True
while True:
    t=shortest[-1]
    for u in edges[t]:
        if distances[u]==distances[t]-1:
            shortest.append(u)
            done[u]=True
            break
    if distances[shortest[-1]]==0:
        break
rets=[-1]*N
c=1
targets=shortest
while targets:
    t=targets.pop()
    if rets[t]!=-1:
        c+=1
        continue
    rets[t]=c
    c+=1
    for u in edges[t]:
        if done[u]: continue
        done[u]=True
        targets.append(t)
        targets.append(u)
print(*rets)
