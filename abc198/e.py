import collections
N=int(input())
colors=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
counts=[0]*(pow(10,5)+1)
done=[False]*N
targets=[(0,True)]
done[0]=True
rets=[]
while targets:
    t,b=targets.pop()
    if b:
        if counts[colors[t]]==0:
            rets.append(t)
        counts[colors[t]]+=1
        for u in edges[t]:
            if not done[u]:
                targets.append((u,False))
                targets.append((u,True))
                done[u]=True
    else:
        counts[colors[t]]-=1
rets.sort()
for ret in rets:
    print(ret+1)
