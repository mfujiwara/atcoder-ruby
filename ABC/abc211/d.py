import collections
MOD=10**9+7
N,M=map(int, input().split())
edges=[set() for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].add(b)
    edges[b].add(a)
targets=collections.defaultdict(int)
targets[0]=1
while targets:
    nexts=collections.defaultdict(int)
    for t in targets:
        n=targets[t]
        for u in edges[t]:
            nexts[u]+=n
            nexts[u]%=MOD
    for t in targets:
        edges[t]=set()
    targets=nexts
    if N-1 in targets:
        break
print(targets[N-1])
