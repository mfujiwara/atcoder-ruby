import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
ret=0
for i,a in enumerate(array):
    counts[a]+=1
    if i>=K:
        counts[array[i-K]]-=1
        if counts[array[i-K]]==0:
            counts.pop(array[i-K])
    if i>=K-1:
        ret=max(ret,len(counts.keys()))
print(ret)
