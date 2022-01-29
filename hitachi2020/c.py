import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
colors=[-1]*N
colors[0]=0
counts=[1,0]
targets=[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        if colors[u]!=-1: continue
        colors[u]=(colors[t]+1)%2
        counts[colors[u]]+=1
        targets.append(u)
stocks=[[] for _ in range(3)]
for i in range(1,N+1):
    stocks[i%3].append(i)
rets=[-1]*N
if counts[0]<=len(stocks[0]):
    for i in range(N):
        if colors[i]==0:
            rets[i]=stocks[0].pop()
        else:
            if stocks[2]:
                rets[i]=stocks[2].pop()
            elif stocks[1]:
                rets[i]=stocks[1].pop()
            else:
                rets[i]=stocks[0].pop()
elif counts[1]<=len(stocks[0]):
    for i in range(N):
        if colors[i]==1:
            rets[i]=stocks[0].pop()
        else:
            if stocks[2]:
                rets[i]=stocks[2].pop()
            elif stocks[1]:
                rets[i]=stocks[1].pop()
            else:
                rets[i]=stocks[0].pop()
else:
    for i in range(N):
        if colors[i]==0:
            if stocks[1]:
                rets[i]=stocks[1].pop()
            else:
                rets[i]=stocks[0].pop()
        else:
            if stocks[2]:
                rets[i]=stocks[2].pop()
            else:
                rets[i]=stocks[0].pop()
print(*rets)
