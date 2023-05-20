import collections
MOD=10**9+7
N=int(input())
edegs=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    edegs[a-1].append(b-1)
    edegs[b-1].append(a-1)
targets=[0]
while targets:
    t=targets.pop()
    for u in edegs[t]:
        edegs[u].remove(t)
        targets.append(u)
dp=[[0]*2 for _ in range(N)]
targets=[0]
while targets:
    t=targets.pop()
    one_more=False
    w=1
    b=1
    for u in edegs[t]:
        if dp[u]==[0,0]:
            one_more=True
            break
        w*=(dp[u][0]+dp[u][1])
        w%=MOD
        b*=dp[u][0]
        b%=MOD
    if one_more:
        targets.append(t)
        for u in edegs[t]:
            targets.append(u)
    else:
        dp[t]=[w,b]        
print(sum(dp[0])%MOD)
