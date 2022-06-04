import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
Q=int(input())
for _ in range(Q):
    x,k=map(int, input().split())
    xxx=set([x])
    for _ in range(k):
        for y in list(xxx):
            xxx|=set(edges[y])
    print(sum(xxx))

