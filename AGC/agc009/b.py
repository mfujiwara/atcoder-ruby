import sys
import collections
sys.setrecursionlimit(500000)
N=int(input())
edges=collections.defaultdict(list) # i は edges[i] に勝った
for i in range(N-1):
    idx=i+1
    a=int(input())-1
    edges[a].append(idx)
memo=[-1]*N
target=[0]
while target:
    t=target.pop()
    if len(edges[t])==0:
        memo[t]=0
    elif memo[edges[t][0]]==-1:
        target.append(t)
        for u in edges[t]:
            target.append(u)
    else:
        rets=[]
        for u in edges[t]:
            rets.append(memo[u])
        rets=sorted(rets)
        for i in range(len(rets)):
            rets[i]+=len(rets)-i
        memo[t]=max(rets)
print(memo[0])
