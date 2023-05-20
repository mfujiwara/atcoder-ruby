import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
group=[-1]*N
targets=[0]
group[0]=0
while targets:
    t=targets.pop()
    for u in edges[t]:
        if group[u]!=-1: continue
        group[u]=0 if group[t]==1 else 1
        targets.append(u)
rets=[]
if group.count(0)>=N//2:
    for i in range(N):
        if group[i]==0:
            rets.append(str(i+1))
            if len(rets)==N//2:
                break
else:
    for i in range(N):
        if group[i]==1:
            rets.append(str(i+1))
            if len(rets)==N//2:
                break
print(" ".join(rets))
