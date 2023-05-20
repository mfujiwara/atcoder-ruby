import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    s,t=map(int, input().split())
    s-=1
    t-=1
    edges[s].append(t)
dp0=[0]*N
for i in range(N-2,-1,-1):
    if edges[i]:
        dp0[i]=sum([dp0[j] for j in edges[i]])/len(edges[i])+1
    else:
        dp0[i]=pow(10,10)
ret=dp0[0]
for target in range(N-2,-1,-1):
    if len(edges[target])<=1: continue
    dp=dp0[:]
    vals=[dp[j] for j in edges[target]]
    maxi=max(vals)
    dp[target]=(sum(vals)-maxi)/(len(edges[target])-1)+1
    for i in range(target-1,-1,-1):
        for j in edges[i]:
            if dp0[j]!=dp[j]:
                dp[i]+=(dp[j]-dp0[j])/len(edges[i])
    ret=min(ret,dp[0])
print(float(ret))
