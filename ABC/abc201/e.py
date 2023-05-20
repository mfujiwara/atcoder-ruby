from collections import defaultdict
MOD=10**9+7
N=int(input())
edges=defaultdict(list)
for _ in range(N-1):
    u,v,w=map(int, input().split())
    edges[u-1].append((v-1,w))
    edges[v-1].append((u-1,w))
group=[[0]*N for _ in range(60)]
for i in range(60):
    group[i][0]=1
targets=[0]
while targets:
    t=targets.pop()
    for u,w in edges[t]:
        if group[i][u]!=0: continue
        for i in range(60):
            if w&(1<<i)>0:
                group[i][u]=-group[i][t]
            else:
                group[i][u]=group[i][t]
        targets.append(u)
ret=0
for i in range(60):
    r=(1<<i)%MOD
    c=group[i].count(1)
    r=r*c%MOD
    r=r*(N-c)%MOD
    ret+=r
    ret%=MOD
print(ret)
