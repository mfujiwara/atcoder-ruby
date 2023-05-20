import collections
N,Q=map(int, input().split())
array=list(map(int, input().split()))
counts=collections.defaultdict(list)
for i,a in enumerate(array):
    counts[a].append(i+1)
for _ in range(Q):
    x,k=map(int, input().split())
    if len(counts[x])>=k:
        print(counts[x][k-1])
    else:
        print(-1)
