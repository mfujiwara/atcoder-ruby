import collections
MOD=998244353
N,M,K=map(int, input().split())
array=list(map(lambda e: int(e)-1, input().split()))
edges=collections.defaultdict(list)
uniq_edges=[]
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
    if u<v:
        uniq_edges.append((u,v))
    else:
        uniq_edges.append((v,u))
counts=collections.defaultdict(int)
for i in range(M-1):
    start=array[i]
    end=array[i+1]
    ret=[]
    targets=[[-1,start]]
    while targets:
        t=targets.pop()
        if t[-1]==end:
            ret=t
            break
        for u in edges[t[-1]]:
            if u==t[-2]: continue
            v=t[:]
            v.append(u)
            targets.append(v)
    for j in range(len(ret)-2):
        u=ret[j+1]
        v=ret[j+2]
        if u>v:
            u,v=v,u
        counts[(u,v)]+=1
dp=[0]*(pow(10,5)*2+1)
dp[pow(10,5)]=1
for edge in uniq_edges:
    k=counts[edge]
    nexts=[0]*(pow(10,5)*2+1)
    for i in range(len(dp)):
        if i>=k:
            nexts[i-k]+=dp[i]
            nexts[i-k]%=MOD
        if i<len(dp)-k:
            nexts[i+k]+=dp[i]
            nexts[i+k]%=MOD
    dp=nexts
print(dp[pow(10,5)+K])
