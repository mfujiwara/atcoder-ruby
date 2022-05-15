import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
targets=[(0,-1)]
done=[False]*N
count=0
while targets:
    t,p=targets.pop()
    if done[t]: continue
    done[t]=True
    count+=1
    if p!=-1:
        print(p+1,t+1)
    if count==N:
        break
    for u in edges[t]:
        if done[u]: continue
        targets.append((u,t))
targets=collections.deque([(0,-1)])
done=[False]*N
count=0
while targets:
    t,p=targets.pop()
    if done[t]: continue
    done[t]=True
    count+=1
    if p!=-1:
        print(p+1,t+1)
    if count==N:
        break
    for u in edges[t]:
        if done[u]: continue
        targets.appendleft((u,t))
