import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
ret=0
for key in counts:
    ret+=(N-counts[key])*counts[key]
print(ret//2)
