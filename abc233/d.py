import itertools
import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
sums=itertools.accumulate(array)
ret=0
counts=collections.defaultdict(int)
counts[K]=1
for s in sums:
    ret+=counts[s]
    counts[K+s]+=1
print(ret)
