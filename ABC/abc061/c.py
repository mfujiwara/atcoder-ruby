import collections
N,K=map(int, input().split())
counts=collections.defaultdict(int)
for _ in range(N):
    a,b=map(int, input().split())
    counts[a]+=b
keys=sorted(list(counts.keys()))
for key in keys:
    K-=counts[key]
    if K<=0:
        print(key)
        exit()
